using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using NetMQ;
using NetMQ.Sockets;
using Newtonsoft.Json;
using System.Text.RegularExpressions;

public class GameManager : MonoBehaviour
{
    BattleDS jsonobj;

    //agent index, material | material 0 is draw material
    public Material[] mVictoryMaterials;
    public GameObject gBattlefieldGameObject;
    //agent index, prefab
    public GameObject[] gSoldierPrefabs;
    GameObject[] gBFarray; //to store references to battlefields

//battlefield name, name of agent, reference to prefab
    Dictionary<int, List<KeyValuePair<string, GameObject>>> soldierAssignment = new Dictionary<int, List<KeyValuePair<string, GameObject>>>();
    int numTroops;

    Vector3 vSpawnLocaiton = new Vector3(0, 0, 10);

    // Start is called before the first frame update
    void Start()
    {
        using (var client = new RequestSocket())
        {
            client.Connect("tcp://localhost:5555");
            client.SendFrame("Hello");
            var message = client.ReceiveFrameString();
            jsonobj = JsonConvert.DeserializeObject<BattleDS>(message);
            Debug.Log(JsonConvert.SerializeObject(jsonobj, Formatting.Indented));
            Debug.Log("Received" + jsonobj.distribution_of_troops[1].distribution[1].battleField);
        }
        numTroops = jsonobj.total_troops;
        spawnBattlefields();
        AssignBattlefields();
        StartCoroutine(timeout());
    }

    IEnumerator timeout()
    {
        yield return new WaitForSeconds(10);
        KillSoldiers();
        stopFighting();
        yield return new WaitForSeconds(5);
        Application.Quit();

    }

    void stopFighting()
    {
        foreach(Results result in jsonobj.After_battle_results)
        {
            List<KeyValuePair<string, GameObject>> tmp =  soldierAssignment[result.battle_field];
            for(int i =0; i < tmp.Count; i++)
            {
                tmp[i].Value.GetComponent<SoldierControl>().stopFighting();
            }
        }
    }
    void KillSoldiers()
    {
        foreach(Results result in jsonobj.After_battle_results)
        {
            // int agent_num = int.Parse(Regex.Match(agent.Name_of_the_Agent, @"[0-9]+").Value);
            List<KeyValuePair<string, GameObject>> tmp =  soldierAssignment[result.battle_field];
            List<KeyValuePair<string, GameObject>> remove_list = new List<KeyValuePair<string, GameObject>>();
            for(int i =0; i < tmp.Count; i++)
            {
                //TODO if result.winner == draw continue
                if(tmp[i].Key != result.winner)
                {
                    Debug.Log(tmp[i].Key +" "+tmp[i].Value);
                    tmp[i].Value.GetComponent<SoldierControl>().KillSoldier();
                    remove_list.Add(tmp[i]);
                }
                
            }
            foreach(KeyValuePair<string, GameObject> rem in remove_list)
            {
                tmp.Remove(rem);
            }
            remove_list.Clear();
            int agent_num = int.Parse(Regex.Match(result.winner, @"[0-9]+").Value);
            gBFarray[result.battle_field-1].GetComponent<MeshRenderer>()
                    .material = mVictoryMaterials[agent_num];
        }
            
    }
    void AssignBattlefields()
    {
        foreach(Agent agent in jsonobj.distribution_of_troops)
        {
            Debug.Log("name of agent: "+agent.Name_of_the_Agent);
            int agent_num = int.Parse(Regex.Match(agent.Name_of_the_Agent, @"[0-9]+").Value);
            foreach(BattlefieldDetails bfd in agent.distribution)
            {
                for(int i= 0; i< bfd.troops; i++)
                {
                    GameObject tmp = Instantiate(gSoldierPrefabs[agent_num-1], vSpawnLocaiton, Quaternion.identity);
                    if(!soldierAssignment.ContainsKey(bfd.battleField))
                    {
                        soldierAssignment.Add(bfd.battleField, new List<KeyValuePair<string, GameObject>>()
                                        {new KeyValuePair<string, GameObject>(agent.Name_of_the_Agent,tmp)});
                    }
                    else
                    {
                        soldierAssignment[bfd.battleField].Add(new KeyValuePair<string, GameObject>(agent.Name_of_the_Agent, tmp));
                    }
                    tmp.GetComponent<SoldierControl>().AssignBattlefield(gBFarray[bfd.battleField-1]
                                    .transform.Find("Center").transform.position);
                }
            }
        }
    }
    void spawnBattlefields()
    {
        float xpos = 0, zpos = 0;
        int numBattlefields = jsonobj.battle_fields;
        gBFarray = new GameObject[numBattlefields];

        for(int i = 0; i< numBattlefields; i++)
        {
            Vector3 position = new Vector3(xpos,0 , zpos);
            if((i+1) % 2 == 0)
            {
                xpos += 5.5f;
                zpos = 0;
            }
            else
            {
                zpos = 5.5f;
            }
            gBFarray[i] = Instantiate(gBattlefieldGameObject, position, Quaternion.identity);
        }
    }
}
