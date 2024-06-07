---
layout: default
title: 7. Dragonking Thordan
parent: Lv 90. DSR
grand_parent: Ultimates
nav_order: 8
has_children: false
has_toc: false
permalink: /ultimates/dsr/07_dragonking_thordan/
---

# Dragonking Thordan

There are a couple of details that we should first go over before going into
the main mechanics loop.

## Mitigations

This phase requires some mitigation planning. To get the most use out of all
the party's cooldowns, you'd do something like the following:

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
<details markdown=block>
<summary>
  <b>[Click to Expand] Mitigation Notation</b>
</summary>
<table>
  <tr>
    <td colspan="2"><b>Party mitigations</b></td>
  </tr>
  <tr>
    <td>MT 90s, ST 90s</td>
    <td><em>Shake It Off, Dark Missionary, Heart of Light, Divine Veil</em></td>
  </tr>
  <tr>
    <td>H1 120s</td>
    <td><em>Temperance, Neutral Sect</em></td>
  </tr>
  <tr>
    <td>H2 30s</td>
    <td><em>Sacred Soil, Kerachole</em></td>
  </tr>
  <tr>
    <td>H2 90s</td>
    <td><em>Deployment Tactics, Zoe</em></td>
  </tr>
  <tr>
    <td>H2 120s</td>
    <td><em>Expedient, Holos</em></td>
  </tr>
  <tr>
    <td>D1, D2</td>
    <td><em>Feint</em></td>
  </tr>
  <tr>
    <td>D3</td>
    <td><em>Troubadour, Tactician, Shield Samba</em></td>
  </tr>
  <tr>
    <td>D4</td>
    <td><em>Addle</em></td>
  </tr>
</table>
</details>
</div>

<table>
  <tr>
    <td><b>Akh Morn's Edge #1</b></td>
    <td>MT Reprisal, H1 120s, H2 30s, D1
      <ul>
        <li>Use H2 30s at the 2nd Trinity after <em>Exaflare's Edge</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><b>Gigaflare's Edge #1</b></td>
    <td>ST Reprisal, H2 30s, D2, D4</td>
  </tr>
  <tr>
    <td><b>Akh Morn's Edge #2</b></td>
    <td>MT Reprisal, MT 90s, ST 90s, H2 30s, D3
      <ul>
        <li>Use MT 90s, ST 90s, H2 30s, D3 at the 2nd Trinity after
        <em>Exaflare's Edge</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><b>Gigaflare's Edge #2</b></td>
    <td>ST Reprisal, H2 30s, D1</td>
  </tr>
  <tr>
    <td><b>Akh Morn's Edge #3</b></td>
    <td>MT Reprisal, MT 90s, ST 90s, H1 120s, H2 30s, D2, D3, D4
      <ul>
        <li>Use MT 90s, ST 90s, D3 as soon as they're available.</li>
      </ul>
    </td>
  </tr>
</table>

Note that there is a need to time some mitigation at the second autoattack
before *Akh Morn's Edge*. This is done to gain additional uses:

- H2 30s will be back for *Gigaflare's Edge*.
- MT 90s, ST 90s, D3 will be back for *Akh Morn's Edge* #3.

---

## Basic Mechanics

Dragonking Thordan has two basic mechanics that are worth mentioning.

### Fire/Ice of Ascalon

All of Dragonking Thordan's major mechanics are combined with either Fire or
Ice of Ascalon, which resolves together at the beginning of the mechanic.

<table>
  <tr>
    <td width="34%">
      <p>If Dragonking Thordan's swords glow <b>red</b>, he will use <em>Fire of
      Ascalon</em>, which is a point-blank AoE.</p>
      <p>Players must be <b>outside</b> his targeting circle.</p>
    </td>
    <td width="33%"><img src="{{site.baseurl}}/assets/images/ultimates/dsr/07/fire_of_ascalon_01.jpg"></td>
    <td><img src="{{site.baseurl}}/assets/images/ultimates/dsr/07/fire_of_ascalon_02.jpg"></td>
  </tr>
  <tr>
    <td width="34%">
      <p>If Dragonking Thordan's swords glow <b>blue</b>, he will use <em>Ice
      of Ascalon</em>, which is a donut AoE.</p>
      <p>Players must be <b>inside</b> his targeting circle.</p>
    </td>
    <td width="33%"><img src="{{site.baseurl}}/assets/images/ultimates/dsr/07/ice_of_ascalon_01.jpg"></td>
    <td><img src="{{site.baseurl}}/assets/images/ultimates/dsr/07/ice_of_ascalon_02.jpg"></td>
  </tr>
</table>

### Trinity

After each mechanic has completed, Dragonking Thordan will auto-attack twice.

<table>
  <tr>
    <td width="50%"><p>Each auto-attack hits <em>three</em> players:</p>
      <ul>
        <li>The player with highest aggro will get hit with dark damage, and
        gain a stack of Dark Resistance Down.</li>
        <li>The player with the second-highest aggro will get hit with light
        damage, and gain a stack of Light Resistance Down.</li>
        <li>The <b>closest</b> player will get hit, and gain a stack of Dark
        Resistance Down, Light Resistance Down, and Physical Vulnerability Up.</li>
      </ul>
    </td>
    <td><img src="{{site.baseurl}}/assets/images/ultimates/dsr/07/trinity.jpg"></td>
  </tr>
</table>

Over the course of the fight, the non-tank players will rotate in to take one
auto-attack each.

<table>
  <tr>
    <td><b>After Exaflare's Edge</b></td>
    <td>D1 → D2</td>
  </tr>
  <tr>
    <td><b>After Akh Morn's Edge</b></td>
    <td>D3 → D4</td>
  </tr>
  <tr>
    <td><b>After Gigaflare's Edge</b></td>
    <td>H1 → H2</td>
  </tr>
</table>

Because of the stacking Light/Dark Resistance Down debuffs on the tanks, the
tanks will be constantly swapping aggro throughout the fight.

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
  <p><b>Tip:</b> It's easy for the tanks to lose track of who is supposed to be
  tanking the boss. To help keep track of things:</p>
  <ul>
    <li>Add text to a Provoke macro so the chat log has a record of who last
    Provoked.</li>
    <li>The tank with <b>0 or 1 stack of Dark Resistance Down</b> should be
    holding aggro.</li>
  </ul>
</div>

With all that setup, we can now go over Dragonking Thordan's major mechanics.

---

## Mechanics Loop

Dragonking Thordan will execute the following loop three times:

1. [Exaflare's Edge](#exaflares-edge)
2. [Akh Morn's Edge](#akh-morns-edge)
3. [Gigaflare's Edge](#gigaflares-edge) *(this will be replaced with*
   *[Morn Afah's Edge](#morn-afahs-edge) on the third loop.)*

### Exaflare's Edge

Have the tank with aggro point Dragonking Thordan either North or South before
the start of this mechanic.

<table>
  <tr>
    <td width="50%">
      <p><b>1.</b> Three Exaflare telegraphs will appear relative to Thordan's
      orientation.</p>
    </td>
    <td><img src="{{site.baseurl}}/assets/images/ultimates/dsr/07/exaflare_01.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>2.</b> Focus on the bright dot at the center of the Exaflares. This
      will be your first dodge point.</p>
      <p>If Dragonking Thordan is facing either north or south, you can also
      use the floor markings to guide your movement.</p>
    </td>
    <td><img src="{{site.baseurl}}/assets/images/ultimates/dsr/07/exaflare_02.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>3.</b> When the Exaflares resolve, dodge to where the bright dot
      was.</p>
    </td>
    <td><img src="{{site.baseurl}}/assets/images/ultimates/dsr/07/exaflare_03.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>4.</b> Continue dodging the next set of Exaflare AoEs.</p>
      <p>Dodging backwards (see the diagram) will <b>always</b> be safe.</p>
      <p>As you get more experienced with the mechanic, you will notice
      Exaflare patterns where you can maintain melee uptime <em>(dodging to the
      left in this case)</em>, but this is not necessary.</p>
    </td>
    <td><img src="{{site.baseurl}}/assets/images/ultimates/dsr/07/exaflare_04.jpg"></td>
  </tr>
</table>

Thordan will then auto-attack twice, which should be taken by the two tanks,
and D1, followed by D2.

The tanks should continue to face Thordan north or south, away from the party.

### Akh Morn's Edge

Thordan will spawn three towers relative to where he is facing:

- One red tower at his front-left
- One red tower front-right
- One blue tower at his rear

The blue tower deals increased damage, and is meant to be taken by the tanks.

All players must be **inside** Thordan's hitbox in order to be within healing
range of both healers- remember to step inside if Thordan's swords were
originally red.

*Akh Morn's Edge* will be resolved with a 3-3-2 split.

<table>
  <tr>
    <td width="50%">
      <ul>
        <li><b>Front-left:</b> H1, D1, D3</li>
        <li><b>Front-right:</b> H2, D2, D4</li>
        <li><b>Back:</b> MT, ST</li>
      </ul>
    </td>
    <td><img src="{{site.baseurl}}/assets/images/ultimates/dsr/07/akh_morn.jpg"></td>
  </tr>
</table>

Thordan will then auto-attack twice, which should be taken by the two tanks,
and D3, followed by D4.

Where Thordan faces after *Akh Morn's Edge* doesn't matter.

### Gigaflare's Edge

<table>
  <tr>
    <td width="50%">
      <p><em>Gigaflare's Edge</em> is a series of three raid-wide AoEs, each
      with an epicenter in a triangle going clockwise or anti-clockwise around
      Dragonking Thordan.</p>
      <p>This is <em>not</em> falloff damage- standing inside the marked region
      <em>(illustrating a South Gigaflare)</em> will one-shot a player, while
      standing outside just deals heavy damage.</p>
      <p>Mitigations for <em>Gigaflare's Edge</em> should be timed as the
      entire sequence lasts 8 seconds, while several debuffs (Reprisal, Feint,
      Addle) lasts only 10 seconds.</p>
    </td>
    <td><img src="{{site.baseurl}}/assets/images/ultimates/dsr/07/gigaflare.jpg"></td>
  </tr>
</table>

Thordan will then auto-attack twice, which should be taken by the two tanks,
and H1, followed by H2.

After *Gigaflare's Edge*, whoever's tanking the boss should face the boss
**directly North or South** to prepare for *Exaflare's Edge*.

The loop then repeats from *Exaflare's Edge*.

---

## Morn Afah's Edge

Dragonking Thordan will put three towers and will continually hit them in quick
order.

As each set of towers kills three players, the party can only take two rounds
of towers as there aren't enough players to take the third set.

A general kill order should resemble:

<table>
  <tr>
    <td><b>First set of towers</b></td>
    <td>H1, H2, MT</td>
  </tr>
  <tr>
    <td><b>Second set of towers</b></td>
    <td>D3, D4, ST</td>
  </tr>
  <tr>
    <td><b>Third set of towers</b></td>
    <td>Ignore <em>(let the tower failed animation wipe the party instead of
    having D1 and D2 killed by the towers.)</em></td>
  </tr>
</table>

Morn Afah's Edge towers will match the Akh Morn's Edge tower groups.

<div style="background-color: #200 ; padding: 10px; border: 1px solid;">
<b>Note:</b> After the first hit, Morn Afah's Edge will continually hit the
towers <b>every 3 seconds</b>- if you're not taking the first set, standby near
your tower, and do not wait to enter when it's your turn!</div>

---

## Buff windows

Assuming the party used potions at the start of P6, the buff/pot window timings
are:

<table>
  <tr>
    <td><b>First buff window</b></td>
    <td>After Gigaflare's Edge #1</td>
  </tr>
  <tr>
    <td><b>Second buff window</b></td>
    <td>During Akh Morn's Edge #3</td>
  </tr>
</table>

Potions can be used at either burst window.

---

## Frequently Asked Questions

<details markdown=block>
<summary>
  <b>[Akh Morn's Edge]</b> Why are we doing 3-3-2 instead of 1-1-6? Wouldn't that make it easier to heal?
</summary>
<table>
  <tr>
    <td>
      <p>1-1-6 at <em>Akh Morn's Edge</em> <b>is</b> easier to heal compared to
      3-3-2, but it does not come for free.</p>
      <p>The biggest obstacle to 1-1-6 is having to mitigate <em>Wyrmsbreath</em>
      2 and <em>Cauterize</em> with the same 30% at the end of P6.</p>
      <ul>
        <li>The tank with a single-target tankbuster needs to time their 30% 
        mitigation at the last second before <em>Wyrmsbreath</em> 2.</li>
        <li>The healers need to top up the tanks (and potentially give targeted
        mitigation)- remember, the tanks are on the other side of the arena 
        during <em>Wyrmsbreath</em>.</li>
      </ul>
      <p>While this is doable, it's much tighter in execution than simply 
      invulning Cauterize, and makes P6 even less forgiving.</p>
      <p>Prog groups <em>especially</em> should aim to get more practice at P7, 
      and it's difficult to justify potentially spending more time in P6 for 
      <em>both</em> tanks to consistently (and independently!) get the timing 
      down.</p>
      <p>Even if Cauterize is properly mitigated, executing 1-1-6 still has some
      intangible tradeoffs. While it <em>is</em> easier to mitigate and heal 
      through, you open up different lines of error:</p>
      <ul>
        <li>Either H2, D2, or D4 forgets and goes to the wrong tower at the 
        wrong <em>Akh Morn's Edge</em>.</li>
        <li>The wrong tank goes to the wrong tower at the wrong <em>Akh Morn's 
        Edge</em>.</li>
        <li>"Less healing" <em>does not</em> mean "no healing", especially 
        given 1-1-6's reputation of "letting healers parse". It's also easy
        for healers to forget that the tank in the DPS tower at <em>Akh 
        Morn's Edge</em> 2 does not have all their cooldowns available because 
        something was used for <em>Akh Morn's Edge</em> 1.</li>
      </ul>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Gigaflare's Edge]</b> Is <em>Gigaflare's Edge</em> really a point-blank 
  AoE, or is it proximity-based damage?
</summary>
<table>
  <tr>
    <td>
      <p><em>Gigaflare's Edge</em> is actually proximity-based, but the 
      falloff is very steep, making it act like an AoE.</p>
      <p>Here's a graph plotting the damage vs distance (in centiyalms).</p>
    </td>
    <td>
      <img src="{{site.baseurl}}/assets/images/ultimates/dsr/07/gigaflare_faq.jpg">
      <em>(Credit: radrauser)</em>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Mitigation]</b> Is there a reason D2 is paired with D4? What happens with
  double caster parties? Wouldn't that overlap Addles?
</summary>
<table>
  <tr>
    <td><p>Pairing D1 with D4 is something I considered, but decided against
    as "D2 Feint first" breaks the usual pattern of D1 > D2.</p>
    <p>That being said, the important part of the mitigation plan is
    establishing the baseline for where D4 uses their Addle. That way, the
    second caster knows where not to Addle (regardless of whether they're D2 or
    D1).</p>
    <p>The same reasoning applies to double-ranged parties.</p>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Burst windows]</b> Why is the first burst window after <em>Gigaflare's
  Edge</em> #1, instead of the P7 opener?
</summary>
<table>
  <tr>
    <td>
      <p>P7 lasts about 3:45 in total, so there's no way to fit in a 
      third 2-minute burst window, even if a reopener was used at the start.</p>
      <p>In addition:</p>
      <ul>
        <li>Some players may have opted to use their burst at the end of P6, 
        after <em>Touchdown</em>.</li>
        <li>Both dragons can also be downed immediately after <em>Touchdown</em> 
        if the party's DPS is high.</li>
      </ul>
      <p>In either scenario, the 2-minute burst abilities may not necessarily be
      available at P7's opener, so setting the first burst after <em>Gigaflare's
      Edge</em> #1 guarantees everyone has their burst abilities ready.</p>
    </td>
  </tr>
</table>
</details>

---

## Troubleshooting

<details markdown=block>
<summary>
  <b>[Akh Morn's Edge]</b> How did my WAR die?
</summary>
<table>
  <tr>
    <td>
      <p>Check that the WAR did not use <em>Shake It Off</em> after
      <em>Vengeance</em>, as <em>Shake It Off</em> removes a WAR's buffs
      (except for <em>Rampart</em>) if used later.</p>
      <p>This is something to pay attention to in the second <em>Akh Morn's
      Edge</em> in particular, as <em>Shake It Off</em> comes back off
      cooldown there after using it at <em>Alternative End</em>.</p>
    </td>
  </tr>
</table>
</details>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
