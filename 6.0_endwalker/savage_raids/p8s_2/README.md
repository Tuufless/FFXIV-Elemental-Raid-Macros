---
layout: default
title: P8S P2
parent: Savage Raids
nav_order: "08_2"
grand_parent: 6.0 Endwalker
permalink: /6.0_endwalker/savage_raids/p8s_2/
---

# Abyssos: The Eighth Circle (Savage) - Part 2

**DISCLAIMER:** *I haven't gotten around to clearing P8S myself yet, so I may be missing some context in the translation below.*

PF uses [Nukemaru's strat](https://youtu.be/RaLfkv-B2Zg), substituting [Hydi/Bijyon's strat for Limitless Desolation](https://youtu.be/8kdGUhXYBJI).

### Japanese

This is [Game8's macro](https://game8.jp/ff14/480771).

*(Nukemaru's strat, Hydi/Bijyon's Limitless Desolation)*
```
【術式1回目(頭割は西)】【術式炎氷(TH西 DPS東) 】
　 　★　　　紫 　 ST│ ▼炎:中央前詰め　▼氷誘導
D1 MT D2　　 MT　│ MT>ST >H1>H2 西 D1>ST
H1　　H2　H1　D2│ D1>D2>D3>D4 東MT>D2
D3 S T D4　 　 D1　│【術式2回目散開 】
※左安置は　H2　D3│　STMT 紫 D3D1
　左右反転→　 D4 　│　　 H1H2D4D2
【概念1回目①】　　【概念1回目②】
　　　　早α　　 　 │　　　遅α
複/遅α　　　　　　│
　　　　　　 早β 　│ 生物　　　　遅β
重/遅βγ　　　　　 │
　　　　早γ　　 　 │　　　遅γ
※4塔：遅αβγ→北で合成
　 　 　 複/重/早余り→南で合成
【万象灰燼：はいじあ/ビジョン式】
　　MT　　D1
ST　 +　　　+　D2　※1,3番塔は前+で範囲捨て
H1　+　　　+　D3　※2,4番塔は後+で範囲捨て
　 　H2　　D4
【概念2回目①】 　 　【概念2回目②】
　　 無/早α　　　 │　　　　遅α
単　　　　　 　 　 │ 生物
　　　　　　早β　│ ｲﾌ ｲﾌ　　　　遅β
複/遅　　　　　　 │ 生物
　　　 早γ 　　 　 │　　　　遅γ
※4塔：遅αβ→北で合成　遅γ/早余り→南で合成
【支配者の一撃】　　　　　【塔優先度】
　MTH1 D3 D1　西>MTSTH1H2D4D3D2D1>東
　ST H2 D4 D2
 ```
 
### English:

*(Nukemaru's strat, Hydi/Bijyon's Limitless Desolation)*
```
【Natural Alignment 1(stack west】
　　 　★　　　　(purple)　ST
　D1 MT D2　　　　　　 MT
　H1　　H2　　　　　H1　D2　※Flip horizontal
　D3 S T D4　　　　　　  D1　　　if west safe
   　　　　　　　　　　H2　D3
　　　　　　　　　　　　D4 
【Fire/Ice(TH west DPS east) 】
▼Fire: Close + forward prio　▼Ice baits prio
　 MT>ST >H1>H2　　　　　　　West： D1>ST
 　D1>D2>D3>D4　　　　　　　East：MT>D2
【Natural Alignment 2 spread 】
　STMT (purple) D3D1
　　 　H1H2D4D2
【High Concept 1-1】【High Concept 1-2】
　　　　8α　　 　 │　　　　　28α
+28α　　　　　 │
　　　　　　 8β 　│(Creation)　　　28β
+28βγ　　　　  │
　　　　8γ　　 　 │　　　　　28γ
※4 towers：　　　28αβγ→Synthesize North
　 　  //Unused 8αβγ→Synthesize South
【Limitless Desolation：Hydi/Bijyon strat】
　　MT　　D1
ST　 +　　　+　D2　※1st, 3rd bait AoE at front +
H1　+　　　+　D3　※2nd, 4th bait AoE at rear +
　 　H2　　D4
【High Concept 2-1】　【High Concept 2-2】
　　 Nothing/7α　　│　　　　　　27α
Solo　　　　　　　　│　Concept
　　　　　　　　　7β│ Ifrit　　Ifrit　　　　27β
/27　　　　　　　  │　Concept
　　　 　　7γ 　　 　 │　　　　　　27γ
※4 Towers：　　　27αβ→Synthesize North
　　　27γ/Unused 7αβ→Synthesize South
【Dominion】　　　　【Tower priority】
　MTH1 D3 D1　W：MTSTH1H2D4D3D2D1：E
　ST H2 D4 D2
 ```

### Markers:

- `1` and `2` are for the two players who are not involved in Natural Alignment's Ice/Fire.
- `ABC` is for αβγ in High Concept
- `D` demarcates the center line for the two stacks in High Concept:
    - North of `D`: 2-man stack (High Concept 1), Solo-man (High Concept 2)
    - South of `D`: 3-man stack (High Concept 1, High Concept 2)

![](images/markers.jpg)
![](images/markers_2.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{"Name":"P8S P2 (Nukemaru)","MapID":884,"A":{"X":100.0,"Y":0.0,"Z":81.5,"ID":0,"Active":true},"B":{"X":118.5,"Y":0.0,"Z":100.0,"ID":1,"Active":true},"C":{"X":100.0,"Y":0.0,"Z":118.5,"ID":2,"Active":true},"D":{"X":81.5,"Y":0.0,"Z":100.0,"ID":3,"Active":true},"One":{"X":100.0,"Y":0.0,"Z":85.0,"ID":4,"Active":true},"Two":{"X":100.0,"Y":0.0,"Z":95.0,"ID":5,"Active":true},"Three":{"X":90.0,"Y":0.0,"Z":90.0,"ID":6,"Active":true},"Four":{"X":110.0,"Y":0.0,"Z":90.0,"ID":7,"Active":true}}
```

</details>

## Timeline
![](https://preview.redd.it/vihvci9rewm91.png?width=1774&format=png&auto=webp&s=82d069cff2ce2a902fa52a1ff23a47310359eb37)
*(Credit: [u/ExiaKuromonji](https://www.reddit.com/r/ffxiv/comments/xa6me7/p8s_part_2_timeline/))*

## Nukemaru's Natural Alignment #1:

Essentially, the Sigil forces the remaining six players into a 2-4 or 4-2 split because it targets two players of the same role (T/H vs DPS).

**Fire** is baited by the three furthest players from the Sigil. The side with 2 players remaining have to figure out their priority between themselves to see who baits Fire:
```
Inside: MT>ST>H1>H2: Outside (baiting Fire)
Inside: D1>D2>D3>D4: Outside (baiting Fire)
```
**Ice** is baited by the two closest players to the Sigil. Because the party is split 2-4 or 4-2, one of the players in the group of 4 (MT, or D1) will have to swap over. The pair that has this player (MT+ST, or D1+D2) are baiting Ice.

i.e: If there are four T/H and two DPS, the MT moves over to the east stack and MT+ST bait Ice. Similarly, if there are two T/H and four DPS, then D1 moves over to the west side and D1+D2 bait Ice.

### Example:

Let's say MT and H2 are both selected to be the Sigils. That means:

Fire: The three pairs are ST>H1 *(the two remaining T/H)*, D1>D2, and D3>D4. In each pair, the lower priority player is baiting Fire on the far side of the line.

Ice: As there are four DPS and two T/H, D1 moves over to join the two T/H. D1 and D2 bait Ice on the near side of the line.

## Limitless Desolation:

Hydi Ai and [Bijyon](https://youtu.be/GA3IWJde15g) proposes the following strategy for Limitless Desolation.

In JP PFs, you might see this:
```
万象灰燼 ビジョン式 はいじあ式
```
It takes advantage of the fact that the first and third set of towers always spawn in the top two rows, while the second and fourth set of towers always spawn in the middle two rows.

[Nukemaru also made a guide](https://youtu.be/8kdGUhXYBJI) explaining the strat.
