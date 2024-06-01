---
layout: default
title: "5a. Run: Dynamis (Delta)"
nav_order: 5
parent: Lv 90. TOP
grand_parent: Ultimates
permalink: /ultimates/top/05_run_dynamis_delta/
---

# Run: Dynamis (Delta Version)

P5 is split up into three "trios"- Delta, Sigma, and Omega. Each trio involves
a series of mechanics before ending with Hello, World debuffs that give players
stacks of Dynamis, needed to clear the final phase.

The strat that PF uses is the "Kinda Awk" strat, that pairs like tethers
together.

---

## Hello, World

The Hello, World debuffs serve as the "big puzzle" over the course of Delta,
Sigma, and Omega. There are a total of four sets of Hello, World debuffs that
the party will need to manage, and the goal is to **have each player enter
the final phase with 3 stacks of Dynamis**.

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
<details markdown=block>
<summary><b>[Click to Expand] Hello, World explanation</b></summary>
<table>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/assets/images/ultimates/top/05a/debuffs/hello_near_world.png">
    </td>
    <td>
      <p><b>Hello, Near World</b></p>
      <ol>
        <li>A large AoE centered on the player with Hello, Near World goes off.</li>
        <li>The debuff then jumps to a second player with a smaller AoE, who is
        the <b>closest</b> player to the player with Hello, Near World.</li>
        <li>The debuff then jumps one more time to the closest player to the
        second player.</li>
      </ol>
      <p>All three players hit gain one stack of Dynamis.</p>
      <p>If an AoE hits two players at the same time, or the player with Hello,
      Near World dies, the party wipes.</p>
      <p><img src="{{site.baseurl}}/assets/images/ultimates/top/05a/hello_near_world.jpg"></p></td>
  </tr>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/assets/images/ultimates/top/05a/debuffs/hello_distant_world.png">
    </td>
    <td><p><b>Hello, Distant World</b></p>
    <ol>
        <li>A large AoE centered on the player with Hello, Distant World goes
        off.</li>
        <li>The debuff then jumps to a second player with a smaller AoE, who is
        the <b>furthest</b> player to the player with Hello, Distant World.</li>
        <li>The debuff then jumps one more time to the furthest player to the
        second player.</li>
      </ol>
      <p>All three players hit gain one stack of Dynamis.</p>
      <p>If an AoE hits two players at the same time, or the player with Hello,
      Distant World dies, the party wipes.</p>
      <p><img src="{{site.baseurl}}/assets/images/ultimates/top/05a/hello_distant_world.jpg"></p></td>
  </tr>
</table>
</details>
</div>

---

## Solar Ray

There are four Solar Rays in this phase. These are two-hit tankbusters that
also apply Magic Vulnerability, forcing either a tank swap, or invuln.

They also hit *extremely* hard (base damage is a little under *three times*
a tank's max HP).

Two of these will be taken with invulnerabilities, and the other two with
mitigations; however, which two will depend on your party composition.

<table>
  <th></th>
  <th>If your party has a WAR</th>
  <th>If your party does not have a WAR</th>
  <tr>
    <td rowspan="2"><b>Before Delta</b></td>
    <td>
      <p>Hallowed Ground > Superbolide > Tank swap + Full buffs</p>
    </td>
      <td>Hallowed Ground > Superbolide > Living Dead
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <em>(N.B: With fast killtimes in P1-P3, Hallowed Ground may not be
      back in time.)</em>
    </td>
  </tr>
  <tr>
    <td><b>Before Sigma</b></td>
    <td>Living Dead > Tank swap + Full buffs</td>
    <td>Superbolide > Living Dead</td>
  </tr>
  <tr>
    <td><b>Before Omega</b></td>
    <td>Holmgang</td>
    <td>
      <p>Tank swap:</p>
      <ul>
        <li>MT: Rampart + healer mitigations</li>
        <li>ST: Rampart + 30%</li>
      </ul>
      <p><em>* Use Rampart when the Arm Lasers go off at the end of Sigma.</em></p>
    </td>
  </tr>
  <tr>
    <td><b>Before Blind Faith</b></td>
    <td>Tank swap + full buffs</td>
    <td>
      <p>Tank swap:</p>
      <ul>
        <li>MT: Rampart + 30%</li>
        <li>ST: Rampart + healer mitigations</li>
      </ul>
    </td>
  </tr>
</table>

Note that the invuln/mitigation order is determined by the tank *jobs*, and
not by the tank *roles*.

<div style="background-color: #200 ; padding: 10px; border: 1px solid;">
  <p><b>Note:</b> There is an edge case where you specifically have:</p>
  <ul>
    <li>WAR + PLD tanks <em>and</em></li>
    <li>Fast killtimes <em>(Hallowed Ground not available for first Solar Ray)</em></li>
  </ul>
  <p>In such a scenario, use <em>Holmgang</em> for the second <em>Solar Ray</em>,
  essentially falling back to the "no WAR" plan. WARs, however, may not be
  familiar with this fallback.</p>
</div>

After the Solar Ray, Omega-M will cast *Run: \*\*\*\*mi\* (Delta Version)*,
which is a *very* hard-hitting raid-wide.

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
  <p><b>Tip:</b> There is ~1:22 between Run Dynamis (Delta Version) and Run:
  Dynamis (Sigma Version).</p>
  <p>Party mitigations that last 15 seconds, and have a 90-second cooldown (tank
  mitigations, D3) can be used immediately after the second Solar Ray hit in
  order to catch Run Dynamis (Delta Version) <em>and</em> be back up in time for
  Run Dynamis (Sigma Version).</p>
  <p>Healer party mitigations last 20 seconds, and can be used to mitigate both
  Solar Ray hits <em>and</em> the follow-up Run Dynamis if timed correctly.</p>
</div>

---

## Run: Dynamis (Delta Version)

Run: Dynamis (Delta Version) can be broken down into three parts:

1. [Rocket Punches](#1-rocket-punches)
2. [Oversampled Wave Cannon and Pile Pitch](#2-oversampled-wave-cannon-and-pile-pitch)
3. [Hello, World](#3-hello-world)

## 1. Rocket Punches

Tethers appear, splitting the party up into two groups:

- Four players will have red/green tethers.
- The other four players will have blue tethers.
  - Hello, Near World and Hello, Distant World will also appear on two players
    with a blue tether.

<table>
  <tr>
    <td width="50%"><p><b>1.</b> Split off into your initial positions:</p>
    <ul>
      <li>
        <p><b>Blue tethers:</b> Form two lines by the "Beetle-form" Omega,
        one long, and one short.</p>
        <p>The "long" tether should be long enough to immediately break once
        the tethers are activated.</p>
      </li>
      <li><b>Red/green tethers:</b> Form two lines by the Reconstructed Omega,
      stretched out to not break the tether.</li>
    </ul></td>
    <td><img src="{{site.baseurl}}/assets/images/ultimates/top/05a/run_dynamis_delta_01.jpg"></td>
  </tr>
  <tr>
    <td><p><b>2.</b> Blue and yellow fists appear above each player.</p>
    <p>The outer pair stays where they are, while the inner pairs move to be in
    line with them.</p>
    <p>The inner pair also adjusts if needed:</p>
    <ol>
      <li>Identify whether you and the player standing next to you (from the
      other tether) have the same-coloured fists.</li>
      <li>If both fists are the same colour, swap positions with your tether
      partner.</li>
    </ol>
    <p><em>In the first example, the blue tethers have the same coloured fists
    together, so the inner tether (H2 and D2) swap sides. There is no swap
    needed for the green tethers, so the inner pair (MT, D1) goes to stack on
    their fist partners (H1 and D4 respectively).</em></p>
    <p><em>In the second example, the green tethers have the same coloured
    fists together, so the inner tether (MT and D1) swap sides. There is no
    swap needed for the blue tethers, so the inner pair (H2, D2) moves to stay
    in line with their fist partners (D3 and ST respectively).</em></p>
    <p><em>At most, only one pair will need to swap.</em></p></td>
    <td>
      <img src="{{site.baseurl}}/assets/images/ultimates/top/05a/run_dynamis_delta_02a.jpg">
      <img src="{{site.baseurl}}/assets/images/ultimates/top/05a/run_dynamis_delta_02b.jpg">
    </td>
  </tr>
  <tr>
    <td><p><b>3.</b> Arms appear on the outside of the arena, and telegraph
    which direction they will spin.</p></td>
    <td><img src="{{site.baseurl}}/assets/images/ultimates/top/05a/run_dynamis_delta_03.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>4.</b> The tethers activate. This will break the outer
      blue-tether.</p>
      <p>The outer blue-tethered players move in to stack with the inner
      blue-tethered players.</p></td>
    <td><img src="{{site.baseurl}}/assets/images/ultimates/top/05a/run_dynamis_delta_04.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>5.</b> The fist telegraphs will appear together with the Eye's beam.</p>
      <p>The Reconstructed Omega will telegraph monitors on one side. One of the
      blue-tethered players will also get Monitors.</p>
      <p>Move to your assigned spinning fist.</p>
      <ul>
        <li><b>Outer blue pair:</b> Bait the arms at the beetle's side.</li>
        <li><b>Inner blue-pair:</b> Break your tether, then go to the middle to
        bait Beyond Defense.</li>
        <li><b>Green-pair nearer  the center:</b> Bait the side arms.</li>
        <li><b>Green-pair at the edge:</b> Bait the arms at the Reconstructed
        Omega's side.</li>
      </ul>
    </td>
    <td><img src="{{site.baseurl}}/assets/images/ultimates/top/05a/run_dynamis_delta_05.jpg"></td>
  </tr>
</table>

## 2. Oversampled Wave Cannon and Pile Pitch

After baiting the outside arm lasers, players are split into two groups based
on their tethers, with each tether group having different responsibilities.

- Red/green tethered players will be **taking monitor hits**.
- Blue tethered players will be handling **Pile Pitch**.

<table>
  <tr>
    <td width="50%">
      <p><b>6.</b> The outer arms will telegraph their AoEs targeting the
      closest player.</p>
      <p>The Omega-M clone hits one of the two closest players with Beyond
      Defense.</p></td>
    <td><img src="{{site.baseurl}}/assets/images/ultimates/top/05a/run_dynamis_delta_06.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>7.</b> The player with Oversampled Wave Cannon Loading points their
      monitors in the other direction of Final Omega's Oversampled Wave Cannon.</p>
      <p>This creates a safe corridor for the three blue-tethered players that
      weren't hit by Beyond Defense to stack together to share Pile Pitch.</p>
      <p>Note that the Pile Pitch stack may or may not include the player with
      Oversampled Wave Cannon Loading.</p>
      <p>The player hit by Beyond Defense stands somewhere within this
      corridor, away from the Pile Pitch stack.</p>
    </td>
    <td><img src="{{site.baseurl}}/assets/images/ultimates/top/05a/run_dynamis_delta_07.jpg"></td>
  </tr>
</table>

## 3. Hello, World

Omega-M and Final Omega will disappear, which is the cue for the last part of
the mechanic, and where players will finally resolve Hello, Near World and
Hello, Distant World.

<table>
  <tr>
    <td colspan="2"><p><b>8.</b> The "beetle" Omega lights up to cleave one side of the
    arena. Move in to the safe side.</p>
    </td>
  </tr>
  <tr>
    <td><b>The green-tether pair towards Beetle Omega</b></td>
    <td>
      <ol>
        <li>Break the tether when the <b>tether's debuff timer reaches 15
        seconds</b>.</li>
        <li>Position to receive Hello, Near World:
          <ul>
            <li>The player on the safe side goes to the <b>edge</b>, at the
            intercardinal position <b>towards</b> Beetle Omega.</li>
            <li>The player on the unside side goes to the <b>marker</b> at
            the intercardinal position.</li>
          </ul>
        </li>
      </ol>
    </td>
  </tr>
  <tr>
    <td><b>The green-tether pair away from Beetle Omega</b></td>
    <td>
      <p>Position to receive Hello, Distant World:</p>
      <ul>
        <li>The player on the unsafe side <b>rotates up to Beetle Omega</b>.</li>
        <li>The player on the safe side goes to the intercardinal mark away
        from Beetle Omega, and three more notches <b>away</b>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><b>Hello, Near World</b></td>
    <td>Stand <b>three rings from the center</b> along the cardinal between
    the two bosses.</td>
  </tr>
  <tr>
    <td><b>Hello, Distant World</b></td>
    <td>Stand at the <b>edge</b> along the cardinal between the two bosses.</td>
  </tr>
  <tr>
    <td><b>The two remaining blue-tethers with no debuff</b></td>
    <td>Go to the <b>edge</b> of the arena at the intercardinal mark away from
    Beetle Omega, and three notches <b>towards</b> Beetle Omega- you will
    <em>not</em> be getting Dynamis stacks this round.</td>
  </tr>
  <td colspan="2">
    <img src="{{site.baseurl}}/assets/images/ultimates/top/05a/run_dynamis_delta_08.jpg">
  </td>
</table>

With everyone in position, the cleave resolves together with Hello, Near World
and Hello, Distant World.

<table>
  <tr>
    <td>
      <p><b>9.</b> Break the final red/green tether when the <b>tether's debuff
      timer reaches 2 seconds</b>.</p>
    </td>
    <td><img src="{{site.baseurl}}/assets/images/ultimates/top/05a/run_dynamis_delta_09.jpg"></td>
  </tr>
</table>

---

## Frequently Asked Questions

<details markdown=block>
<summary>
  <b>[Solar Ray]</b> Can you mitigate both Solar Ray and Run: Dynamis with
  party mitigations?
</summary>
<table>
  <tr>
    <td>
      <p>Only healer 120s mitigations last long enough (20 seconds) to cover
      both Solar Ray and Run: Dynamis.</p>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Solar Ray]</b> If we don't have a WAR, why don't we alternate between
  invulning and mitigating <em>Solar Ray</em>? Wouldn't that be easier?
</summary>
<table>
  <tr>
    <td>
      <p>This is a tradeoff to prepare for P6.</p>
      <p>You <em>can</em> alternate between invulning and mitigating Solar Rays
      in P5, but doing so leads to problems later on in P6.</p>
      <p>First, only two tanks can invuln the Solar Ray before Run: Dynamis
      (Omega) and have their invuln back in P6- DRK and WAR, so if your party
      is PLD + GNB, you're out of luck and have to invuln the first two Solar
      Rays in P5 to invuln anything in P6.</p>
      <p>This means we are left with DRK + (PLD/GNB), and we have to make a
      choice whether the Living Dead the second Solar Ray (before Sigma), or
      the third Solar Ray (before Omega).</p>
      <p>If a DRK spends Living Dead on the third Solar Ray, Living Dead will
      only be available for the final tankbuster in P6, leading to the
      following base mitigation plan:</p>
      <ul>
        <li>[~0:00] Cosmo Dive #1 → Rampart</li>
        <li>[~0:46] Wave Cannon #1 → Shadow Wall</li>
        <li>[~1:20] Wave Cannon #2 → Rampart</li>
        <li>[~1:54] Cosmo Dive #2 → Living Dead</li>
      </ul>
      <p>This, however, has the following problems:</p>
      <ul>
        <li>Cosmo Dive has a high roll of about 280k base damage. In comparison,
        Wave Cannon hits much harder, with a high roll of 370k base damage
        <em>(that is not a typo!)</em>. As a result, additional resources will
        need to be dedicated to the DRK taking Wave Cannon with Rampart.</li>
        <li>Rampart will not be naturally off cooldown between Cosmo Dive #1 and
        Wave Cannon #2. The DRK will need to time the first Rampart so that it
        catches the Cosmo Dive at the end just so Rampart will be back up in time
        for Wave Cannon #2.</li>
        <li>The party is actively scrambling to coordinate party mitigation so that
        the party does not die to damage, yet alone give the DRK more mitigation to
        survive Wave Cannon #2 with Rampart. It's easier to move that fuss to P5's
        Solar Rays when there's less going on, and it's easier for the healers to
        pay more attention to the tanks.</li>
      </ul>
      <p>By not alternating between invulning and mitigating Solar Rays in P5, you
      get to do a much simpler base mitigation plan in P6 where things are more
      hectic:</p>
      <ul>
        <li>[~0:00] Cosmo Dive #1 → Rampart</li>
        <li>[~0:46] Wave Cannon #1 → ST invuln, MT 30%</li>
        <li>[~1:20] Wave Cannon #2 → MT invuln, ST 30%</li>
        <li>[~1:54] Cosmo Dive #2 → Rampart</li>
      </ul>
      <p>This doesn't apply if your party has a WAR, as WAR is the <em>only</em>
      tank that can invuln the Solar Ray before Run: Dynamis (Omega) and have it
      back up for a Wave Cannon.</p>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Solar Ray]</b> If we have DRK + WAR, why do we use Living Dead at the
  second Solar Ray (before Sigma) instead of following PLD and GNB and
  invulning the first?
</summary>
<table>
  <tr><td><p>This is just a matter of convenience- the interval between Delta
  and Sigma is a 2-minute window, and spending Living Dead here means fewer
  buttons for the DRK to press during the burst window.</p></td></tr>
</table>
</details> 

<details markdown=block>
<summary>
  <b>[Delta (Awk)]</b> Is there a reason why blue tethers go opposite
  Final Omega instead of beside it, or is this an arbitrary choice?
</summary>
<table>
  <tr>
    <td>
      <p>Putting the blue tethers opposite Final Omega gives them the best
      vantage point for Final Omega's Oversampled Wave Cannon.</p>
      <p>This is important, as the blue tether players will be the ones
      resolving Beyond Defense → Pile Pitch together with Final Omega's (and a
      player's) Oversampled Wave Cannon.</p>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Hello, World]</b> Can Hello, World jump back to the original player?
</summary>
<table>
  <tr><td><p>Yes. If the original player with Hello, Near World or Hello,
  Distant World is the nearest (or furthest) player after the first bounce, it
  will bounce back to the original player, killing them.</p></td></tr>
</table>
</details>
<details markdown=block>
<summary>
  <b>[Hello, World]</b> What happens if a player that already has three stacks
  of Dynamis gets a Hello, World jump?
</summary>
<table>
  <tr><td><p>Nothing- Dynamis is capped at three stacks.</p></td></tr>
</table>
</details>

## Troubleshooting

<details markdown=block>
<summary>
  <b>[Delta]</b> The blue/yellow fists AoEs are missing and we get hit by
  Unmitigated Explosion- what happened?
</summary>
<table>
  <tr>
    <td>
      <p>The fist AoEs only appear <em>if and only if</em> a blue fist is
      correctly stacked with a yellow fist.</p>
      <p>This is done pair-wise, so players who <em>have</em> fist AoEs did it
      correctly.</p>
    </td>
  </tr>
</table>
</details>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
