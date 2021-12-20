# Rock Paper Scissors

## Model Plan

- Rock, paper, scissors is a **game** played by **two participants**
- The game consists of **rounds**
- In each round, a **participant** chooses a **symbol** from **rock**, **paper**, or **scissors**, and the other **participant** does the same.
- Then a **winner** of the round is determined by **comparing** the chosen symbols.
- The **rules** of the game state that rock wins over scissors, scissors beats (cuts) paper, and paper beats (covers) rock.
- The winner of the round is awarded a **point**.
- The game goes on for as many rounds as the participants agreed on.
- The winner is the participant with the most points.

- `input processing output`

| Phase    | Actor       | Behavior        | Data              |
|-------   |-------------|---------------  |-------------------|
| input    | participant | chooses symbol  |symbol chosen      |
|processing|  GameRules  | decides winner  | winner            |
|          |             | based on symbols|                   |
|processing| GameRules   | awards point    | participant points|
|output    |  Game       |  declares winner| games won         |
|output    |  Game       | decides restart | game restarted    |
