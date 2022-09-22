/ name, race, gender, team, hitpoints
class Player {
  #name;
  #race;
  #gender;
  #team;
  #hitpoints;
  
  constructor(n, r, g, h)
  {
    this.name = n;
    this.race = r;
    this.gender = g;
    this.hitpoints = h;
  }
  
  get_name() {
    return this.name;
  }
  get_race() {
    return this.race;
  }
  get_gender() {
    return this.gender;
  }
  get_team() {
    return this.team;
  }
  get_hitpoints() {
    return this.hitpoints;
  }
  
  team_up(t) {
    this.team = t;
  }
  
  take_damage(d) {
    this.hitpoints = this.hitpoints - d;
    if (this.hitpoints < 0)
      this.hitpoints = 0;
  }
  
  attack(monster) {
    if (this.hitpoints > 0)
    {
      monster.take_damage(1);
    }
  }
}

class Monster {
  #name;
  #race;
  #hitpoints;
  
    constructor(n, r, h)
  {
    this.name = n;
    this.race = r;
    this.hitpoints = h;
  }

  get_name() {
    return this.name;
  }
  get_race() {
    return this.race;
  }
  get_hitpoints() {
    return this.hitpoints;
  }
  
  take_damage(d) {
    this.hitpoints = this.hitpoints - d;
    if (this.hitpoints < 0)
      this.hitpoints = 0;
  }
  
  attack(player)
  {
    if (this.hitpoints < 1)
       return;
    player.take_damage(2);
    for (let p of player.get_team())
      {
        if (p.get_name() != player.get_name())
        {
          p.take_damage(1);
        }
      }
  }
}

p1 = new Player("P1", "P", "M", 10);
p2 = new Player("P2", "P", "M", 15);
m1 = new Monster("M1", "M", 35);
team = [p1, p2];
p1.team_up(team);
p2.team_up(team);

console.log("Start ============================");
for (const p of team){
  console.log(`Player ${p.get_name()}: ${p.get_hitpoints()}`);
};
console.log(`Monster ${m1.get_name()}: ${m1.get_hitpoints()}`)

let round = 1;
while (m1.get_hitpoints() > 0 && p1.get_hitpoints() > 0 && p2.get_hitpoints() > 0)
 {
    //p1.take_damage(1);
   console.log(`Round ${round}: -----------------`)
    for (let p of team){
      p.attack(m1);
      m1.attack(p);
    }
    for (const p of team){
      console.log(`Player ${p.get_name()}: ${p.get_hitpoints()}`);
    };
    console.log(`Monster ${m1.get_name()}: ${m1.get_hitpoints()}`);
   round += 1;
 }
console.log("End ============================");
