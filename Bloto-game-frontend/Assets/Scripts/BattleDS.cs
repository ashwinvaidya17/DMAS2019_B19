using System.Collections.Generic;
public class BattleDS
{
    public string Game;
    public string Implementation;
    public int battle_fields;
    public int total_troops;
    public int total_players;
    public string max_wins;

    public List<Agent> distribution_of_troops = new List<Agent>();
    public List<Results> After_battle_results = new List<Results>();

}

public class Results
{
    public int battle_field, troops_remaining;
    public string winner;
}
public class Agent
{
    public string Name_of_the_Agent;
    public List<BattlefieldDetails> distribution = new List<BattlefieldDetails>();

}

public class BattlefieldDetails
{
    public int battleField;
    public int troops;
}