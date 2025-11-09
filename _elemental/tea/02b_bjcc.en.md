---
layout: default
title: 2b. Brute Justice + Cruise Chaser
parent: Lv 80. TEA (Elemental)
permalink: /elemental/tea/02b_bjcc/
---

# Brute Justice + Cruise Chaser

My preferred method of doing this phase is using [my Tollgate strat](https://na.finalfantasyxiv.com/lodestone/character/10898230/blog/4941271/)
that is very similar to MOOF's strat that stacks both bosses in the middle.

The "Tollgate" name comes from the third Nisi pass, where the tanks and healers
line up to take/pass Nisi. Someone mentioned that passing Nisi here felt like
passing through a tollgate, and the name stuck.

The strat simplifies the Water/Lightning and Nisi passes, **but at the cost of
increased Tank damage.** This phase is already one of the more
healing-intensive fights, so be prepared.

Tanks should try to have minor cooldowns available for the Lightning passes.

<table>
  <tr>
    <td width="50%">
      <p>At a basic level, the tanks will keep both bosses stacked in the
      center, with some healer movement.</p>
      <p>The DPS make up much of the movement in this phase.</p>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/bjcc_overview.jpg">
    </td>
  </tr>
</table>

---

## Mechanics

This phase contains two "hot potato" loops that the party must handle 
simultaneously.

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
<details markdown=block>
<summary><b>[Click to Expand] Loop 1: Compressed Water/Lightning breakdown</b></summary>
<p>These are two 30-second debuffs that are applied on two players when Brute 
Justice casts <em>Link-up</em>.</p>
<p>When the timer expires, the debuffs explode in a shared-damage AoE 
(<em>Crashing Wave</em> and <em>Crashing Thunder</em>), centered on the 
affected player.</p>
<ul>
  <li>If the player with the debuff ever dies, the debuff explodes and wipe the 
  raid.</li>
  <li>After the explosion, the debuff transfers to a random player that was hit.</li>
  <li>If the debuff cannot be passed to a new player this way (e.g: nobody else
  was hit), it explodes and wipes the raid.</li>
  <li>The player that originally had the debuff gets an elemental resistance
  down debuff, so they <em>cannot</em> participate in two stacks of the same 
  element in a row.</li>
</ul>
<table>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/debuffs/compressed_water.png">
    </td>
    <td>
      <p><b>Compressed Water</b></p>
      <ul>
        <li>Starts on a <b>random healer</b>.</li>
        <li>The more players that are hit, the less damage each player takes.</li>
        <li>At least three players should share the Water stack damage.</li>
        <li>A waterspout will also spawn where the debuffed player was standing.
        <ul>
          <li>Players that move or stay too near this waterspout will be
          instantly killed.</li>
          <li>The waterspout must either be frozen with Brute Justice's Ice, or 
          destroyed with fire from Brute Justice's <em>Flarethrower</em>.
          Failing to do so will wipe the raid.</li>
        </ul>
      </li>
    </ul>
  </td>
  </tr>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/debuffs/compressed_lightning.png">
    </td>
    <td>
      <p><b>Compressed Lightning</b></p>
      <ul>
        <li>Starts on a <b>random DPS</b>.</li>
        <li>The more players that are hit, the <b>more damage</b> each player
        takes.</li>
        <li>For this reason, we want <b>exactly two players</b> in each 
        Lightning stack <em>(the person with <em>Compressed Lightning</em>, and 
        the person we want to pass it to.)</em>.</li>
      </ul>
    </td>
  </tr>
</table>
</details>
</div>

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
<details markdown=block>
<summary><b>[Click to Expand] Loop 2: Nisi breakdown</b></summary>
<p>These are DoTs that are applied on either all the DPS, or all the tanks and 
healers when Brute Justice casts Judgment Nisi.</p>
<table>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/debuffs/final_decree_nisi_alpha.png">
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/debuffs/final_decree_nisi_beta.png">
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/debuffs/final_decree_nisi_gamma.png">
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/debuffs/final_decree_nisi_delta.png">
    </td>
    <td>
      <p><b>Final Decree Nisi αβγδ</b></p>
      <ul>
        <li>If a player with Nisi touches a player without Nisi, the player
        without Nisi gains a fresh copy of the Nisi they just touched.</li>
        <li>If two players with <b>different coloured</b> Nisis touch each
        other, they are instantly killed.</li>
      </ul>
    </td>
  </tr>
</table>
<p>During the fight, Brute Justice will cast Verdict, which sets up for a 
checkpoint later in the phase when it casts Gavel.</p>
<p>When Verdict is cast, it applies the following additional debuffs on all 
players:</p>
<table>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/debuffs/final_judgment_decree_nisi_alpha.png">
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/debuffs/final_judgment_decree_nisi_beta.png">
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/debuffs/final_judgment_decree_nisi_gamma.png">
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/debuffs/final_judgment_decree_nisi_delta.png">
    </td>
    <td><p><b>Final Judgment Decree Nisi αβγδ</b></p>
      <ul>
        <li>Each Final Judgment Decree Nisi debuff goes onto two players- one
        tank/healer, and one DPS.</li>
        <li>All eight players <b>must have the corresponding Nisi debuff</b> on 
        them when <em>Gavel</em> finishes its cast, or <em>Gavel</em> will
        result in a wipe.</li>
      </ul>
    </td>
  </tr>
</table>
</details>
</div>

The party must keep both debuff loops going, passing *Compressed Water*, 
*Compressed Lightning*, and all Nisis around until Brute Justice casts *Gavel*, 
which removes all the debuffs.

---

<table>
  <tr>
    <td width="50%">
      <p><b>1.</b> Initial positions.</p>
      <ul>
        <li><b>MT</b>: Take Cruise Chaser.</li>
        <li><b>ST</b>: Take Brute Justice.</li>
      </ul>
      <p><em>(Note the MT and ST starting positions are swapped from the usual
      convention. The bosses each tank takes spawns on their respective
      starting side.)</em></p>
      <p>Cruise Chaser will cast <em>Whirlwind</em>, while Brute Justice will
      cast <em>Judgment Nisi</em> which debuffs the party with Nisis,
      <em>Compressed Water</em>, and <em>Compressed Lightning</em>.</p>
      <p>Stand as close as you can towards the center of the arena, without
      passing Nisi debuffs.</p>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/bjcc_01.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>2.</b> Two Chakrams will spawn directly opposite one another at any
      of the eight intercardinal directions and target a random party member's
      position.</p>
      <p>Move towards the edge of the arena to dodge the Chakrams' path.</p>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/bjcc_02.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>3.</b> When the Chakrams go off, Cruise Chaser will cast
      <em>Optical Sight</em>, targeting large baited AoEs on all players
      current positions.</p><p>All players move back to the center.</p>
      <p>The tanks will swap sides.</p>
      <ul>
        <li><b>ST</b>: Enter the inner circle first, but yield to allow the
        <b>MT</b> to pass.</li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/bjcc_03.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>4.</b> Cruise Chaser will stop to cast <em>Photon</em>.</p>
      <p><b>This is a shield check</b> as <em>Photon</em> will bring all
      player's health down to 1HP. If there are no shields, the DoT from the
      Nisis will kill their players.</p>
      <ul>
        <li><b>MT:</b> Cross over to the west side. <em>(Cruise Chaser will not
        follow, but you can spend a few GCDs on Brute Justice while waiting.)</em></li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/bjcc_04.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>5.</b> The two tanks should use this time to try and center the
      bosses, particularly the ST that's holding Brute Justice.</p>
      <p><em>(Use the arrowheads on the side of the boss's targeting circles to
      help)</em></p>
      <p>The bosses don't <em>really</em> need to be centered N/S, but should
      be centered E/W.</p>
      <p>After Photon is cast is the <b>first Nisi pass</b>.</p>
      <ul>
        <li><b>MT</b>, <b>D1</b>: Do not pass Nisi yet.</li>
        <li><b>ST</b>, <b>D2</b>: Pass Nisi with each other.</li>
        <li><b>H1</b>, <b>D3</b>: Pass Nisi with each other.</li>
        <li><b>H2</b>, <b>D4</b>: Pass Nisi with each other.</li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/bjcc_05.jpg">
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/brute_justice_position.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>6.</b> Cruise Chaser casts Spin Crusher.</p>
      <ul>
        <li><b>MT</b>: Dodge Spin Crusher and pass Nisi with D1.</li>
        <li><b>H1</b>, <b>H2</b>: The healer <em>with</em> Water goes to the
        first Water position (H1 in this example). The healer <em>without</em>
        Water can preposition to bait Fire and the Hidden Mine.</li>
        <li><b>D1</b>: Note D1 is <em>never</em> involved in the first Water
        stack.</li>
        <li><b>D3</b>: Be careful if you have the first Lightning as your path
        may cross D2's path to the Water stack.</li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/bjcc_06.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>7. First Water/Lightning pass</b>.</p>
      <ul>
        <li><b>Water:</b> Healer + at least two of D2, D3, D4 (excluding
        whoever had Lightning)</li>
        <li><b>Lightning:</b> DPS → ST</li>
        <li><b>D1</b>: You may need to avoid the Lightning explosion by moving
        towards the MT.</li>
      </ul>
      <div style="background-color: #002 ; padding: 10px; border: 1px solid;">
      <b>Tip:</b> If tanks pop <em>Rampart</em> just before the first
      Water/Lightning, it will mitigate the Lightning, autoattacks from Cruise
      Chaser/Brute Justice, the upcoming <em>Hidden Mine</em> if the tanks are
      quick, <em>and</em> be back up in time for <em>Double Rocket Punch</em>
      at the end of the phase.</div>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/bjcc_07.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>8.</b> After Water resolves, Healers and DPS move to prepare for
      <em>Hidden Mines</em> and <em>Enumeration</em>.</p>
      <ul>
        <li><b>D2</b>: Move under the bosses, between the two tanks.</li>
        <li><b>D3</b>: Move behind the MT</li>
        <li><b>D4</b>: Move behind the ST.</li>
      </ul>
      <p>All DPS should stay within the sector marked by the green dotted line:</p>
      <ul>
        <li>This prevents the DPS baiting the Hidden Mines by accident.</li>
        <li>This prevents the DPS from getting hit by the Hidden Mines when
        they explode later.</li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/bjcc_08.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>9.</b> This is the most involved step for everybody in this phase.</p>
      <p><b>Tanks:</b> One tank (at random) will be chosen to resolve Ice.</p>
      <ul>
        <li>If a player gets too close to the water tornado, the tornado will
        tether to the player, knocking them back and dealing very high damage
        (one-shotting them).</li>
        <li>The Ice puddle should be dropped so that it <b>just misses the
        Water tornado</b> <em>(see image)</em>. The Ice puddle will then expand
        once and freeze the tornado.</li>
      </ul>
      <p><b>Healers:</b> Bait Fire puddles and Hidden Mines before joining the
      <em>Enumeration</em> groups.</p>
      <ul>
        <li><b>H1</b>: Always west Enumeration.</li>
        <li><b>H2</b>: Always east Enumeration.</li>
      </ul>
      <p><b>DPS:</b> Resolve Enumeration with the Healers.</p>
      <p>If either side has both Enumerations (or equivalently, no
      Enumerations), D1 and D2 swap sides.</p>
      <ul>
        <li><b>D1</b>: West Enumeration unless a swap is needed.</li>
        <li><b>D2</b>: East Enumeration unless a swap is needed.</li>
        <li><b>D3</b>: Always west Enumeration.</li>
        <li><b>D4</b>: Always east Enumeration.</li>
      </ul>
      <p>All non-tanks should stay inside the sector marked by the green dotted
      line <em>(note it has expanded since the Hidden Mines have been baited)</em>.</p>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/bjcc_09.jpg">
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/bjcc_ice.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>10.</b> After resolving Ice (if applicable), tanks wait for the
      <em>Hidden Mine</em> to drop first, before taking the <em>Hidden
      Mine</em> on their side. This is a heavy AoE tankbuster.</p>
      <p>Healers and DPS should stay inside the sector marked by the green
      dotted line to avoid getting clipped by the Hidden Mine's AoE.</p>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/bjcc_10.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>11. Second Nisi pass.</b></p>
      <p>Melee + Tanks be careful as the Ice will expand.</p>
      <ul>
        <li><b>MT</b>, <b>ST</b>: Pass Nisi with the nearest melee on your side
        (they may have swapped sides)</li>
        <li><b>D1</b>, <b>D2</b>: Pass Nisi with the nearest tank on your side
        (you may have swapped sides)</li>
        <li><b>H1</b>, <b>D3</b>: Pass Nisi with each other.</li>
        <li><b>H2</b>, <b>D4</b>: Pass Nisi with each other.</li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/bjcc_11.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>12. Second Water + Lightning pass.</b></p>
      <ul>
        <li><b>Water:</b> All DPS</li>
        <li><b>Lightning:</b> ST → MT</li>
      </ul>
      <ul>
        <li><b>MT</b>: Face Cruise Chaser west after receiving Lightning to
        prepare for the <em>Plasma Shield</em>.</li>
      </ul>
      <p>Keep in mind that Cruise Chaser will autoattack the MT after this
      Lightning pass.</p>
      <p><b>Brute Justice casts Verdict</b>, which gives all players their
      <em>Final Judgment Decree Nisi</em> debuffs which determines the next two
      Nisi passes.</p>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/bjcc_12.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>13.</b> Cruise Chaser casts <em>Limit Cut</em>, which will spawn a
      Plasma Shield in front of Cruise Chaser.</p>
      <p>Meanwhile, Brute Justice will prepare <em>Flarethrower</em>, which we
      will use to destroy the waterspout left behind by the 2nd Water.</p>
      <ul>
        <li><b>MT:</b> Face Cruise Chaser west until Cruise Chaser starts
        casting <em>Limit Cut</em> (which will spawn the Plasma Shield).</li>
        <li><b>ST:</b> <b>Stay close to Brute Justice</b> and point Brute
        Justice south to hit the waterspout with <em>Flarethrower</em>.</li>
        <li><b>DPS:</b> Destroy the Plasma Shield. The Plasma Shield can
        <b>only be damaged from the front</b>.</li>
      </ul>
      <p>Tanks and Healers line up to form the "tollgate" while the DPS
      destroys the Plasma Shield.</p>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/bjcc_13.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>14. Third Nisi pass</b>.</p>
      <p>After the Plasma Shield is destroyed, the DPS pass through this
      "tollgate" to pass Nisi with the appropriate tank/healer before gathering
      in the south-east corner for the third Water pass.</p>
      <ul>
        <li>The DPS that was the second Water passes Nisi to their partner, but
        does <b>not</b> cross the tollgate, returning west instead.</li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/bjcc_14.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>15. Third Water + Lightning pass</b>.</p>
      <ul>
        <li>Water: All DPS (except 2nd Water) + H2</li>
        <li>Lightning: MT → H1</li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/bjcc_15.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>16. Fourth Nisi pass</b>.</p>
      <p>Tank and healer positions are fixed (MT > H1 > ST > H2). DPS pass with
      the appropriate tank or healer.</p>
      <ul>
        <li><b>MT</b>: Pull Cruise Chaser to the east of the Ice block.</li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/bjcc_16.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>17.</b> Cruise Chaser casts <em>Propeller Wind</em>.</p>
      <p>Players must use the frozen Ice to block line-of-sight to Cruise
      Chaser, or they will become confused and run around uncontrollably.</p>
      <ul>
        <li><b>MT</b>: Join the Nisi lineup.</li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/bjcc_17.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>18.</b> Cruise Chaser casts <em>Photon</em>, bringing both tanks
      down to 1HP.</p>
      <p>Brute Justice then prepares <em>Double Rocket Punch</em>, a two-man
      shared tankbuster.</p>
      <ul>
        <li><b>D3</b>: Bait Brute Justice's Super Jump south.</li>
      </ul>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/bjcc_18.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>19.</b> Brute Justice targets the furthest player and casts
      <em>Apocalyptic Ray</em>.</p>
    </td>
	  <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/bjcc_19.jpg">
    </td>
  </tr>
</table>

After the *Apocalyptic Ray*, Cruise Chaser casts two *Whirlwinds* (one after
the other) before both bosses start casting their enrage (*Eternal Darkness* 
and *Final Sentence*).

If either boss dies, the other starts casting their enrage.

---

## Passing Nisi (after Verdict)

Here are some examples on passing Nisis during the third pass.

At this time, either all the tanks and healers have Nisi (who the DPS need to
collect the appropriate Nisis from), or the DPS have all the Nisis (which they
need to pass to the appropriate tank or healer).

<table>
  <tr>
    <td width="50%">
      <p><b>Example 1:</b> Tanks/Healers have Nisi.</p>
      <p><b>Third pass:</b></p>
      <ul>
        <li>DNC collects orange Nisi from WHM.</li>
        <li>SAM collects purple Nisi from WAR.</li>
        <li>RPR collects green Nisi from SGE.</li>
        <li>SMN collects blue Nisi from DRK.</li>
      </ul>
      <p><b>Fourth pass:</b></p>
      <ul>
        <li>DNC passes orange Nisi to SGE.</li>
        <li>SAM passes purple Nisi to WAR.</li>
        <li>RPR passes green Nisi to DRK.</li>
        <li>SMN passes blue Nisi to WHM.</li>
      </ul>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/nisi_example_01.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>Example 2:</b> Tanks/Healers have Nisi.</p>
      <p><b>Third pass:</b></p>
      <ul>
        <li>NIN collects orange Nisi from SGE.</li>
        <li>RPR collects green Nisi from PLD.</li>
        <li>MCH collects purple Nisi from WHM.</li>
        <li>RDM collects blue Nisi from DRK.</li>
      </ul>
      <p><b>Fourth pass:</b></p>
      <ul>
        <li>NIN passes orange Nisi to DRK.</li>
        <li>RPR passes green Nisi to WHM.</li>
        <li>MCH passes purple Nisi to SGE.</li>
        <li>RDM passes blue Nisi to PLD.</li>
      </ul>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/nisi_example_02.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>Example 3:</b> DPS have Nisi.</p>
      <p><b>Third pass:</b></p>
      <ul>
        <li>RDM passes blue Nisi to WHM.</li>
        <li>MNK passes purple Nisi to PLD.</li>
        <li>RPR passes green Nisi to DRK.</li>
        <li>MCH passes orange Nisi to SGE.</li>
      </ul>
      <p><b>Fourth pass:</b></p>
      <ul>
        <li>RDM collects green Nisi from DRK.</li>
        <li>MNK collects blue Nisi from WHM.</li>
        <li>RPR collects purple Nisi from PLD.</li>
        <li>MCH collects orange Nisi from SGE.</li>
      </ul>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/nisi_example_03.jpg">
    </td>
  </tr>
  <tr>
    <td>
      <p><b>Example 4:</b> DPS have Nisi.</p>
      <p><b>Third pass:</b></p>
      <ul>
        <li>RDM passes orange Nisi to PLD.</li>
        <li>MNK passes purple Nisi to WHM.</li>
        <li>RPR passes blue Nisi to DRK.</li>
        <li>MCH passes green Nisi to SGE.</li>
      </ul>
      <p><b>Fourth pass:</b></p>
      <ul>
        <li>RDM collects orange Nisi from PLD.</li>
        <li>MNK collects purple Nisi from WHM.</li>
        <li>RPR collects blue Nisi from DRK.</li>
        <li>MCH collects green Nisi from SGE.</li>
      </ul>
    </td>
    <td>
      <img src="{{site.baseurl}}/images/ultimates/tea/02b/nisi_example_04.jpg">
    </td>
  </tr>
</table>

---

## Frequently Asked Questions

<details markdown=block>
<summary>
<b>[Tank swap]</b> Why don't we do a Provoke swap instead of having the two
tanks cross each other (especially with Nisi)?</summary>
<table>
  <tr>
    <td>
      <p>Two reasons:</p>
      <ol>
        <li>If a tank happens to die in <em>Limit Cut</em> and gets raised at
        the start of BJCC, their first instinct is to <em>Provoke</em>
        whichever boss they're supposed to hold. Now that <em>Provoke</em> is 
        on cooldown, it cannot be used to swap the bosses after Chakrams go
        off.</li>
        <li>Cruise Chaser stops to cast <em>Photon</em>. If you swap bosses 
        using <em>Provoke</em>, the tank that Provokes Brute Justice can only
        attack Cruise Chaser, and either has to hold damage, potentially steal
        hate back, or resort to stance dancing tricks that is more trouble than
        it is worth.</li>
      </ol>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
<b>[Hidden Mines]</b> Why doesn't D3 bait the west Hidden Mine instead of H1?
</summary>
<table>
  <tr>
    <td>
      <p>The objective is to have both Enumeration targets visible and in close
      proximity to one another.</p>
      <p>Suppose D3 and H2 baited the Hidden Mines instead and D2 and D3 were
      targeted for Enumeration.</p>
      <p>D2 only sees the Enumeration on D2, but now has to look at D3 to
      determine whether they need to switch positions with D1, with two giant
      robots in the center blocking the view.</p>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
<b>[Hidden Mines]</b> Why don't we bait the Hidden Mines towards the outer edge
of the arena? Doesn't that put the healers further away from Brute Justice so a
ranged DPS doesn't bait a Hidden Mine by mistake?</summary>
<table>
  <tr>
    <td>
      <p>The idea is to keep both bosses in the center. In particular, if the
      West mine is baited towards the edge, the MT has to pull Cruise Chaser
      closer to the edge in order to take the Hidden Mine, and doesn't leave
      much space for the DPS to fit in for the Plasma Shield.</p>
      <p>Of course, you could have the MT and ST switch sides again to recenter
      the bosses, but that violates a different principle which is to try and
      keep the tanks and healers to their half of the arena as much as
      possible.</p>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
<b>[Plasma Shield]</b> Why are all four DPS on the Plasma Shield? Isn't that
overkill?
</summary>
<table>
  <tr>
    <td>
      <p>Yes, it's overkill.</p>
      <p>You really only need three DPS to destroy the Plasma Shield in time,
      but this is a single point of failure and having all four DPS on the
      shield is insurance against someone targeting the wrong thing by
      accident, or one of the DPS angled too far from the shield's front so
      they don't do any damage.</p>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
<b>[Gavel]</b> What happens if you kill Brute Justice before <em>Gavel</em>?
</summary>
<table>
  <tr>
    <td>
      <p>Alas, this is not feasible- if Brute Justice dies before
      <em>Gavel</em> resolves, he does an instantcast <em>Final Sentence</em>
      on the way out, killing everybody <em>even if</em> the debuffs from
      <em>Verdict</em> have not yet been assigned.</p>
      {% include youtube.html id="VStb1QTG6vc" %}
    </td>
  </tr>
</table>
</details>

---

## Troubleshooting

<details markdown=block>
<summary>
<b>[Crashing Thunder]</b> Why did this deal more damage than usual?
</summary>
<table>
  <tr>
    <td>
      <p>Water and Lightning work differently.</p>
      <p>While <em>Crashing Wave</em> works like any other stack damage (damage
      is lowered as more people are hit by <em>Crashing Wave</em>), Lightning 
      is the opposite; damage <em>increases</em> as more people are hit by
      <em>Crashing Thunder</em>.</p>
      <p>This is why we want the Lightning stacks to contain exactly two 
      players.</p>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary><b>[Compressed Water]</b> What is "Severe Contamination"?</summary>
<table>
  <tr>
    <td>
      <p>This is the pulsing raid-wide damage that you get if the waterspout
      left behind from <em>Compressed Water</em> is not frozen or destroyed
      by <em>Flarethrower</em>.</p>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
<b>[Hidden Mines]</b> What went wrong with the Hidden Mine baits? Why was a 
mine baited on the DPS instead of a healer?
</summary>
<table>
  <tr>
    <td>
      <p>The Hidden Mines are baited by the two furthest players from Brute
      Justice, which should be the healers.</p>
      <p>If a DPS ended up baiting the Hidden Mine, it is likely because:</p>
      <ul>
        <li>A DPS was outside the green sector marked in Step 7 above
        <em>or</em></li>
        <li>The ST did not position Brute Justice in the center of the
        arena.</li>
      </ul>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary><b>[Plasma Shield]</b> How did the MT get one-shot?</summary>
<table>
  <tr>
    <td>
      <p>Cruise Chaser gains a damage-up buff if the Plasma Shield is not
      destroyed in time, and its auto-attack will one-shot the MT.</p>
      <p>Even if the MT survives this, the follow-up Whirlwind (before
      third Water) will wipe the party.</p>
    </td>
  </tr>
</table>
</details>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
