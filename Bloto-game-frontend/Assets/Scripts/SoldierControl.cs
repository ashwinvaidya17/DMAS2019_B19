using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class SoldierControl : MonoBehaviour
{
    NavMeshAgent agent;
    Vector3 location;
    bool stoppedFighting = false;


    void Update()
    {
        float distanceToTarget = Vector3.Distance(transform.position, location);
        if( distanceToTarget < 1)
        {
            this.gameObject.GetComponent<Animator>().SetBool("Walk", false);
            Fight();
        }

    }
    public GameObject killEffect;
    public void AssignBattlefield(Vector3 loc)
    {
        agent = this.gameObject.GetComponent<NavMeshAgent>();
        location = loc;
        agent.destination = location;
        this.gameObject.GetComponent<Animator>().SetBool("Walk", true);

    }

    void Fight()
    {
        if(!stoppedFighting)
            this.gameObject.GetComponent<Animator>().SetBool("Fight", true);
    }

    public void stopFighting()
    {
        this.gameObject.GetComponent<Animator>().SetBool("Fight", false);
        stoppedFighting = true;
    }

    public void KillSoldier()
    {
        //Instantiate(killEffect, this.transform.position, Quaternion.identity);
        Destroy(this.gameObject);
    }
}
