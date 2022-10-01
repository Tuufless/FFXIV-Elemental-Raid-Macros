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

PF uses [Nukemaru's strat](https://youtu.be/RaLfkv-B2Zg), substituting [Hydi/Bijyon's strat for Limitless Desolation](#limitless-desolation).

The combination is often nicknamed "**Nukehai**" (ぬけはい).

## Game 8's macro

The following is [Game8's macro](https://game8.jp/ff14/480771), which follows Nukemaru's strat.

### Japanese

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

## Lambda Unendlich's macro

 This is slightly modified version of [Lambda Unendlich's macro](https://ffxiv.link/078732) for the same strat (substituting in Game8's Limitless Desolation), but goes into a little more detail about some of the mechanics:

### Japanese

*(Nukemaru's strat, Hydi/Bijyon's Limitless Desolation)*
```
【術式記述1回目】
デバフ持ち→A、他→2待機　頭割りからの場合は西受け
 <1回目の散開>       |　<2回目の散開>
　　　   ◎　            | ST  　　◎　　  ST
　　MT　  ST          |　 　MT     MT
　D1　　　 D2       | D2        H1        D2
　H1　        H2       |　　 D1　   D1
       D3　  D4          | D3 　   H2　　 D3
　　　　　　　　   ｜　　D4　   D4
 <炎処理>
 ②/①     　     ①/②　※西側TH   MT>ST>H1>H2
　　　　◎　　　　　　東側DPS D1>D2>D3>D4
 ④/③              ③/④　　上記優先度で番号順に配置
 誘導：②④
 <氷処理> ※MTD1調整
 西側：タンヒラ　東側：DPS
 西側誘導：D1>ST　東側誘導：MT>D2
【概念支配1回目】
 <1回目デバフ処理>　 　＜2回目デバフ処理＞
　　　　 早α　　　   |　　　　遅α
複/遅α　　　　　　  |
　　　　　　　 早β   |　生物　　　　遅β　※マカA>B>C順で複>重
重/遅βγ　　　　　   |　　　　　　　　　　　完成概念がいない場所へ
　　　　 早γ　　　   |　　　　遅γ
 <塔処理優先度> 
1回目：北>α>β>γ>南
2回目：北>遅α>遅β>遅γ>他>南
【万象灰燼：はいじあ/ビジョン式】
　　MT　　D1
ST　 +　　　+　D2　※1,3番塔は前+で範囲捨て
H1　+　　　+　D3　※2,4番塔は後+で範囲捨て
　 　H2　　D4
【術式記述2回目】
　<散開>　　　　　　　　　＜頭割り＞
　   MT    ◎     D3　D1　　　　中央
ST
　   H1　H2　D4　D2
【概念支配2回目】
 <1回目デバフ処理>　 　＜2回目デバフ処理＞
　　　 無/早α　　    |　　　　遅α
単　　　　　　          |　生
　　　　　　　 早β   | ｲﾌ  ｲﾌ　　　　遅β
複/遅　　　　　        |　生
　　　　 早γ　　　   |　　　　遅γ
 <塔処理優先度>
1回目：北>α>β>γ>南　無→3で合成
2回目：北>遅α>遅β>遅γ>早αβγ>南
【支配者の一撃】
MT　H1　D3　D1
 ST　H2　D4　D2
 塔処理：西MTSTH1H2D4D3D2D1東
```

### English

*(Nukemaru's strat, Hydi/Bijyon's Limitless Desolation)*
```
【Natural Alignment 1】
Debuffs→A、Others→Standby at 2　If stack first, resolve West
 <Spread 1st>       |　<Spread 2nd>
　　　   ◎　            | ST  　　◎　　  ST
　　MT　  ST          |　 　MT     MT
　D1　　　 D2       | D2        H1        D2
　H1　        H2       |　　 D1　   D1
       D3　  D4          | D3 　   H2　　 D3
　　　　　　　　   ｜　　D4　   D4
 <Forcible Trifire>
 ②/①　　　 ①/②　※①②③④ priority：
　　　　◎　　　　　　T/H West：MT>ST>H1>H2
 ④/③　　　 ③/④　　  DPS East：D1>D2>D3>D4
　Baits：②④
 <Forcible Difreeze> ※MTD1 baits
　West：T/H　East：DPS
West Bait：D1>ST　East Bait：MT>D2
【High Concept 1】
　 <1st Debuffs>　 　＜2nd Debuffs＞
　　　　 8α　　　   |　　　　28α
+28α　　　　　　|
　　　　　　　 8β   |　(Animal)　　28β　※> replaces players
+28β+28γ　　　|　　　　　　　　　　　that formed a creation
　　　　 8γ　　　   |　　　　28γ　　　　　from A>B>C
 <Tower priority>
　1st：N：α > β > γ：S
　2st：N：Slow α > Slow β > Slow γ > Others：S
【Limitless Desolation：Hydi/Bijyon strat】
　　MT　　D1
ST　 +　　　+　D2　※1st, 3rd bait AoE at front +
H1　+　　　+　D3　※2nd, 4th bait AoE at rear +
　 　H2　　D4
【Natural Alignment 2】
　<Spread>　　　　　　　　　＜Stack＞
　   MT    ◎     D3　D1　　　　mid
ST
　   H1　H2　D4　D2
【High Concept 2】
　<1st Debuffs>　 　＜2nd Debuffs＞
　 Nothing/7α　    |　　　　　27α
Solo　　　　　　　|　Concept
　　　　　　　 7β   | Ifrit　Ifrit　　　　27β
/27βγ　　　        |　Concept
　　　　 7γ　　　   |　　　　　27γ
 <Tower priority>
1st set：N:α>β>γ:S　Nothing→Synthesize at 3
2nd set：N:27α>27β>27γ>7αβγ:S
【Dominion】
MT　H1　D3　D1
 ST　H2　D4　D2
 Towers：(West)MTSTH1H2D4D3D2D1(East)
```

## Markers:

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

## Nukemaru's Natural Alignment

Here's a breakdown for the Fire/Ice portion in Nukemaru's Natural Alignment.

<table>
  <tr>
    <td><p>These are the base positions for all players during Natural Alignment.</p><p>Two players of the same role (T/H vs DPS) will be selected as the <b>Sigils</b> (the players with the purple mark), forcing the remaining six players into a 2-4 or a 4-2 split.</p></td>
    <td><img src="images/natural_alignment.jpg"></td>
  </tr>
</table>

**Fire** is baited by the three <b>furthest</b> players from the Sigil.

- The side with 4 players take up their base positions as above.
- The side with 2 players have to figure out the priority between themselves to see who baits Fire:
```
Inside: MT>ST>H1>H2: Outside (baits Fire)
Inside: D1>D2>D3>D4: Outside (baits Fire)
```
<table>
  <tr>
    <td><p><b>Example 1:</b> MT and ST are selected as the Sigils.</p>
    <p>The remaining pairs are:<ul><li>H1 > H2</li><li>D1 > D2</li><li>D3 > D4</li></ul>In each pair, the player with the lower priority baits Fire (H2, D2, D4).</p></td>
    <td><img src="images/natural_alignment_ex1_fire.jpg"></td>
  </tr>
  <tr>
    <td><p><b>Example 2:</b> D1 and D4 are selected as the Sigils.</p>
    <p>The remaining pairs are:<ul><li>MT > ST</li><li>H1 > H2</li><li>D2 > D3</li></ul>In each pair, the player with the lower priority baits Fire (ST, H2, D3).</p></td>
    <td><img src="images/natural_alignment_ex2_fire.jpg"></td>
  </tr>
</table>

**Ice** is baited by the two **closest** players to the Sigil.

- Because the party is split 2-4 or 4-2, one of the players in the group of 4 will have to move to the other group to make it an even 3-3 split. This will **either** be the MT (if T/H have four players), or D1 (if DPS have four players)
- The melee pair from the side that has four players (MT+ST, or D1+D2) baits Ice.

<table>
  <tr>
    <td><p><b>Example 1:</b> MT and ST are selected as the Sigils.</p>
    <p><ul><li>The DPS side has four players, so D1 moves to the other side.</li><li>D1 and D2 bait Ice.</li></ul></p></td>
    <td><img src="images/natural_alignment_ex1_ice.jpg"></td>
  </tr>
  <tr>
    <td><p><b>Example 2:</b> D1 and D4 are selected as the Sigils.</p>
    <p><ul><li>The T/H side has four players, so MT moves to the other side.</li><li>MT and ST bait Ice.</li></ul></p></td>
    <td><img src="images/natural_alignment_ex2_ice.jpg"></td>
  </tr>
</table>

There is a variant that also does [Natural Alignment on just one tile](https://youtu.be/Gkk5GsqC5dY) instead of two, making it easier to heal, but makes positioning stricter.

## Nukemaru's High Concept #1

<table>
  <tr>
    <td><p>Note that the colour combinations are fixed.</p>
    <p><ul>
      <li>Green = α + β</li>
      <li>Blue = α + γ</li>
      <li>Purple = β + γ</li>
    </ul></p>
    </td>
    <td><img src="images/animal_concepts.jpg"></td>
  </tr>
</table>

This is Nukemaru's strat for High Concept #1. Note that αβγ are placed at **cardinal** positions instead of intercardinals, allowing players to naturally determine their North-South priorities when resolving various parts of High Concept.

<table>
  <tr>
    <td><p><b>1.</b> All players take up their starting positions.</p>
    <p><ul><li><b>7αβγ:</b> North, East, South respectively.</li><li><b>2-man stack + 27α:</b> 1/2 a tile north of West.</li><li><b>3-man stack + 27β + 27γ:</b> 1/2 a tile south of West.</li></ul></p></td>
    <td><img src="images/high_concept_1_ex1_1.jpg"></td>
  </tr>
  <tr>
    <td><b>2.</b> AoEs resolve.</td>
    <td><img src="images/high_concept_1_ex1_2.jpg"></td>
  </tr>
  <tr>
    <td><p><b>3.</b> Two coloured towers spawn. Everyone gather up for heals.</p>
    <p><ul><li><b>7αβγ:</b> If you need to fuse, meet in the center to create the animal concept.</li></ul></p><p><em>In this example, the towers are purple, so 7β and 7γ will fuse.</em></p></td>
    <td><img src="images/high_concept_1_ex1_3.jpg"></td>
  </tr>
  <tr>
    <td><p><b>4.</b> The boss will cleave one half of the arena.</p><p>Once the two players have created the animal concept, they split to take the two towers while dodging the boss's AoE.</p><p><b>If you came from the top side, you will take the top tower.</b></p><p><em>In this example, 7β came from above 7γ, so 7β takes the north tower. The boss is also cleaving east here.</em></p></td>
    <td><img src="images/high_concept_1_ex1_4.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>5.</b> After the cleave goes off, everyone takes up position for the second set of AoEs.</p>
      <p>
        <ul>
          <li><b>27αβγ:</b> North, East, South respectively.</li>
          <li><b>7αβγ:</b>
            <ul>
              <li><b>If you fused:</b> Go 1/2 tile north/south of west. <b>If you came from the top side, you will take the northern position.</b></li>
              <li><b>If you did not fuse:</b> Return to your original starting position.</li>
            </ul>
          </li>
          <li><b>2-man and 3-man stacks:</b> Replace the two players that fused earlier. <b>The 2-man stack replaces the "more north" player.</b></li>
        </ul>
      </p>
      <p><em>In this example:
        <ul>
          <li>7α did not fuse earlier, so they return North.</li>
          <li>7β and 7γ fused:
            <ul>
              <li>7β goes west and takes the north position.</li>
              <li>7γ goes west and takes the south position.</li>
              <li>The 2-man stack takes 7β's position (east).</li>
              <li>The 3-man stack takes 7γ's position (south).</li>
            </ul>
          </li>
        </ul>
      </em></p>
    </td>
    <td><img src="images/high_concept_1_ex1_5.jpg"></td>
  </tr>
  <tr>
    <td><b>6.</b> Second round of AoEs resolve.</td>
    <td><img src="images/high_concept_1_ex1_6.jpg"></td>
  </tr>
  <tr>
    <td><p><b>7.</b> Four coloured towers spawn.</p>
    <p><b>If you need to fuse:</b>
      <ul>
        <li><b>27αβγ:</b> Go between the two north towers.</li>
        <li><b>Others:</b> Go between the two south towers.</li>
      </ul>
    </p>
    <p><em>In this example, the towers are blue, so the players at α and γ will fuse.
      <ul>
        <li>27α fuses with 27γ north.</li>
        <li>The players that <b>were</b> with 27α and 27γ fuse south.</li>
      </ul></em>
    </p></td>
    <td><img src="images/high_concept_1_ex1_7.jpg"></td>
  </tr>
  <tr>
    <td><p><b>8.</b> The boss will cleave one half of the arena again.</p><p>Once each pair have created the animal concept, they split to take the two towers while dodging the boss's AoE.</p><p><b>The player that came from the top side takes the top tower.</b></p><p><em>In this example:<ul><li>The two players that came from α take the top towers</li><li>The two players that came from γ take the bottom towers.</li><li>The boss is cleaving west.</li></ul></em></p></td>
    <td><img src="images/high_concept_1_ex1_8.jpg"></td>
  </tr>
</table>

## Limitless Desolation:

Hydi Ai and [Bijyon](https://youtu.be/GA3IWJde15g) proposes the following strategy for Limitless Desolation.

It takes advantage of the fact that the first and third set of towers always spawn in the top two rows, while the second and fourth set of towers always spawn in the middle two rows.

[Nukemaru also made a guide](https://youtu.be/8kdGUhXYBJI) explaining the strat.

## Nukemaru's High Concept #2

This is Nukemaru's strat for High Concept #2. Several concepts from High Concept #1 carry over to High Concept #2.

<table>
  <tr>
    <td><p><b>1.</b> All players take up their starting positions.</p>
    <p>
      <ul>
        <li><b>7αβγ:</b> North, East, South respectively.</li>
        <li><b>27αβγ:</b>
          <ul>
            <li><b>Solo stack:</b> 1/2 a tile north of West.</li>
            <li><b>Other 27αβγ:</b> 1/2 a tile south of West <em>(one of the two remaining 27αβγ will be a 2-man stack)</em>.</li>
          </ul>
        </li>
        <li><b>No debuff:</b> North</li>
      </ul>
    </p>
    <p><em>In this example, 27β has the solo stack.</em></p></td>
    <td><img src="images/high_concept_2_ex1_1.jpg"></td>
  </tr>
  <tr>
    <td><b>2.</b> AoEs resolve.</td>
    <td><img src="images/high_concept_2_ex1_2.jpg"></td>
  </tr>
  <tr>
    <td><p><b>3.</b> Two coloured towers spawn.</p>
    <p><ul>
        <li><b>7αβγ:</b> If you need to fuse, meet in the center to create the animal concept, just like High Concept #1. This time around, <b>7γ will <em>always</em> be involved in this fusion.</b></li>
        <li><b>No debuff:</b> Fuse together North-West to make Ifrit.</li>
      </ul>
      <p>Ifrit players will suffer from continuous DoT damage until the end of High Concept, and need to be kept alive by the healers until then.</p>
      </p><p><em>In this example, the towers are purple, so 7β and 7γ will fuse.</em></p></td>
    <td><img src="images/high_concept_2_ex1_3.jpg"></td>
  </tr>
  <tr>
    <td><p><b>4.</b> The boss will cleave one half of the arena.</p><p>Once the two players have created the animal concept, they split to take the two towers while dodging the boss's AoE.</p><p><b>If you came from the top side, you will take the top tower.</b></p><p><em>In this example, 7β came from above 7γ, so 7β takes the north tower. The boss is also cleaving east here.</em></p></td>
    <td><img src="images/high_concept_2_ex1_4.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>5.</b> After the cleave goes off, everyone takes up position for the second set of AoEs.</p>
      <p>
        <ul>
          <li><b>27αβγ:</b> North, East, South respectively.</li>
          <li><b>7αβγ:</b> The one that did <b>not</b> fuse earlier returns to their original starting position.</li>
          <li><b>Ifrits + Animal Concepts:</b> Take up the "T-shape" formation as shown.</li>
        </ul>
      </p>
      <p><em>In this example, 7α did not fuse earlier, so they return North.</em></p>
    </td>
    <td><img src="images/high_concept_2_ex1_5.jpg"></td>
  </tr>
  <tr>
    <td><b>6.</b> Second round of AoEs resolve.</td>
    <td><img src="images/high_concept_2_ex1_6.jpg"></td>
  </tr>
  <tr>
    <td><p><b>7.</b> Four coloured towers spawn, along with four shades at the four cardinal directions.</p>
    <p>
      <ul>
        <li><b>Ifrits + Animal Concepts:</b> Split up in your formation, and tether to one shade each.</li>
        <li><b>27αβ:</b> Go between the two north towers.</li>
        <li><b>27γ + Unused 7αβγ:</b> Go between the two south towers.</li>
      </ul>
    </p>
    <p><em>In this example, 7α was not used in the first fusion, so they will go south to fuse with 27γ.</em></p></td>
    <td><img src="images/high_concept_2_ex1_7.jpg"></td>
  </tr>
  <tr>
    <td><p><b>8.</b> The shades will each fire a beam in the direction of the player they were tethered to.</p>
    <p>
      <ul>
        <li><b>Ifrits + Animal Concepts:</b> Rotate clockwise to drag your tethered shade along the outer row/column. Note that the four corners of the arena will not be safe, because they will get hit by two beams.</li>
        <li>Each pair in the center needs to take the corresponding pair of coloured towers in the center four tiles. Note that the coloured towers will be in a <b>random configuration</b>.
          <ul>
            <li><b>The player that came from the northern side prioritizes the North, then West tower if there is a tie.</b></li>
          </ul>
        </li>
      </ul>
    </p></td>
    <td><img src="images/high_concept_2_ex1_8.jpg"></td>
  </tr>
  <tr>
    <td><p><b>9.</b> The two Ifrit players then combine with the two birds in the center to form four Phoenix feathers.</p><p>The four Phoenix feathers will then tether together and fuse to form Phoenix, which gives the Phoenix concept to all players in the party.</p><p><b>All party members must be topped to 100% HP before this final Phoenix fusion completes.</b></p></td>
    <td><img src="images/high_concept_2_ex1_9.jpg"></td>
  </tr>
</table>