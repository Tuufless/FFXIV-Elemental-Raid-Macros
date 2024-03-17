---
layout: default
title: A. Mitigation
parent: Lv 90. DSR
nav_order: 9
has_children: false
has_toc: false
grand_parent: Ultimates
permalink: /ultimates/dsr/mitigation/
---

# Appendix A: Mitigation

The following is a mitigation framework for the encounter.

It is *not* a plan for every single cooldown available to the party; instead,
think of the following as a bare-bones framework to work with- i.e: these are
the things that people will generally look for when mitigation is missing.

<table>
  <th width="50%">Mitigation by Phase</th>
  <th colspan=2>Mitigation by Role</th>
  <tr>
    <td>
      <ul>
        <li><a href="#p2-thordan">P2. Thordan</a></li>
        <li><a href="#p3-nidhogg">P3. Nidhogg</a></li>
        <li><a href="#p4-eyes--saving-haurchefant">P4. Eyes + Saving Haurchefant</a></li>
        <li><a href="#p5-alternate-timeline-thordan">P5. Alternate Timeline Thordan</a></li>
        <li><a href="#p6-double-dragons">P6. Double Dragons</a></li>
        <li><a href="#p7-dragonking-thordan">P7. Dragonking Thordan</a></li>
      </ul>
    </td>
    <td>
      <ul>
        <li><a href="#mt">MT</a></li>
        <li><a href="#st">ST</a></li>
        <li><a href="#h1">H1</a></li>
        <li><a href="#h2">H2</a></li>
      </ul>
    </td>
    <td>
      <ul>
        <li><a href="#d1">D1</a></li>
        <li><a href="#d2">D2</a></li>
        <li><a href="#d3">D3</a></li>
        <li><a href="#d4">D4</a></li>
      </ul>
    </td>
  </tr>
</table>

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
<details markdown=block>
<summary>
  <b>[Click to Expand] Mitigation Notation</b>
</summary>
<table>
  <tr>
    <td>Tank 30%</td>
    <td>Vengeance, Sentinel, Shadow Wall, Nebula</td>
  </tr>
  <tr>
    <td>Tank 3rd</td>
    <td>Thrill of Battle, Bulwark, Oblation, Camouflage</td>
  </tr>
  <tr>
    <td>Tank 90s</td>
    <td>Shake It Off, Dark Missionary, Heart of Light, Divine Veil</td>
  </tr>
  <tr>
    <td>H1 120s</td>
    <td>Temperance, Neutral Sect</td>
  </tr>
  <tr>
    <td>H1 180s</td>
    <td>Liturgy of the Bell, Macrocosmos</td>
  </tr>
  <tr>
    <td>H2 30s</td>
    <td>Sacred Soil, Kerachole</td>
  </tr>
  <tr>
    <td>H2 90s</td>
    <td>Deployment Tactics, Zoe</td>
  </tr>
  <tr>
    <td>H2 120s</td>
    <td>Expedient, Holos</td>
  </tr>
  <tr>
    <td>Extra</td>
    <td>
      <p>Anything that cannot be reliably present in a party.</p>
      <ul>
        <li>Passage of Arms, Fey Illumination, Collective Unconsciousness,
        Consolation, Panhaima, Dismantle, Improvisation, Magick Barrier</li>
      </ul>
    </td>
  </tr>
</table>
</details>
</div>

## Mitigation by Phase

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
  The raw damage values have also been provided, separated into damage dealt
  to:
  <ul>
    <li><b>T</b>anks (MT, ST)</li>
    <li><b>P</b>hysical DPS (D1, D2, D3)</li>
    <li><b>M</b>agic (H1, H2, D4)</li>
  </ul>
</div>

Physical DPS jobs have higher max HP, but lower magic defense compared to
casters.

- Tanks have 93k max HP.
- Physical DPS jobs have 64k max HP.
- Magical jobs have 58k max HP.
- Basic shields *(Succor, Eukrasian Prognosis)* absorb 7k damage.

### P2. Thordan

Notably, the mitigations below have been planned *without* taking the healer
120s into consideration, so they can be used wherever needed for comfort.

<table>
  <tr>
    <td>
      <p>3x Ascalon's Might</p>
      <ul>
        <li><b>T:</b> 3x 71k-85k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT short</li>
        <li>ST Reprisal, D1</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>A WAR can Holmgang this instead.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Strength of the Ward</p>
      <ul></ul>
    </td>
    <td>
      <ul>
        <li><b>MT + ST:</b> 30% + short</li>
        <li>D3</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Ancient Quaga</p>
      <ul>
        <li><b>P:</b> 78k-90k</li>
        <li><b>M:</b> 73k-82k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, ST 90s, H2 30s, D4</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>This is the latest the tanks can use their 90s and have them back by 
        <em>Ultimate End</em> and <em>Final Chorus</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Heavenly Heel → Ascalon's Might x3</p>
      <ul>
        <li><b>T:</b> 165k-175k</li>
        <li><b>T:</b> 3x 71k-85k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><b>MT + ST:</b> Rampart + 3rd</li>
        <li>ST Reprisal, D2</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Tank swap MT→ST.</li>
        <li>MT's short mitigation may not be available for <em>Heavenly
        Heel</em>, but the ST's short will be back for <em>Ascalon's
        Might</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Sanctity of the Ward</p>
      <ul>
        <li><b>P:</b> 85k-104k</li>
        <li><b>M:</b> 85k-104k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>H2 90s</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>This is the latest healers can use their 120s to have it back for
        an <em>Eye of the Tyrant</em> stack in P3.</li>
        <li>Use H2 90s before the third cleave of <em>Ascalon's Might</em> to 
        guarantee it will be back for <em>Final Chorus</em>.</li>
        <li>This is a common place for a SGE to <em>Panhaima</em>. SGE can also
        use <em>Kerachole</em> here.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Ultimate End</p>
      <ul>
        <li><b>P:</b> 73k-103k</li>
        <li><b>M:</b> 68k-97k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, MT 90s, H2 30s, D1, D4</li>
      </ul>
    </td>
    <td></td>
  </tr>
</table>

### P3. Nidhogg

<table>
  <tr>
    <td>
      <p>Final Chorus</p>
      <ul>
        <li><b>P:</b> 94k-104k</li>
        <li><b>M:</b> 88k-97k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>ST 90s, H2 30s, H2 90s, D3</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>
          <p>This needs one more extra mit (<em>Collective Unconsciousness</em>,
          <em>Passage of Arms</em>, <em>Magick Barrier</em>, <em>Improvised
          Finish</em>, etc.) to guarantee survival with a SGE.</p>
          <p>Abilities that boost healing (<em>Physis II</em>, <em>Asylum</em>,
          <em>Nature's Minne</em>, <em>Mantra</em>) also help here.</p>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Eye of the Tyrant #1</p>
      <ul>
        <li><b>P:</b> 66k-84k</li>
        <li><b>M:</b> 61k-74k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>ST Reprisal, H2 30s <em>or</em> H2 120s</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>A SCH can use <em>Seraph</em> to help cover both <em>Eye of the
        Tyrant</em> stacks.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Eye of the Tyrant #2</p>
      <ul>
        <li><b>P:</b> 66k-84k</li>
        <li><b>M:</b> 61k-74k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, D2, H2 30s <em>or</em> H2 120s</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>D2 adds <em>Feint</em> to the second <em>Eye of the Tyrant</em>
        instead of the first because two players would take damage from the
        towers.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Soul Tethers</p>
      <ul>
        <li><b>T:</b> 226k-262k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><b>MT + ST:</b> Invuln</li>
      </ul>
    </td>
    <td></td>
  </tr>
</table>

### P4. Eyes + Saving Haurchefant

<table>
  <tr>
    <td>
      <p>Hatebound</p>
      <ul>
        <li><b>P:</b> 29k-41k</li>
        <li><b>M:</b> 27k-37k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT 90s, D3</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>This is to help with healing since there isn't a good spot
        elsewhere.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Steep in Rage</p>
      <ul>
        <li><b>P:</b> 55k-66k</li>
        <li><b>M:</b> 53k-61k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT <em>Reprisal</em></li>
      </ul>
    </td>
    <td>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Brightwing #1</p>
      <ul>
        <li><b>P:</b> 49k-65k</li>
        <li><b>M:</b> 49k-63k</li>
      </ul>
    </td>
    <td></td>
    <td>
      <ul>
        <li>Covered by the Tank LB3.</li>
        <li>H2 90s will be up for <em>Wrath of the Heavens</em> if used 
        immediately after getting pulled in.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Brightwing #2</p>
      <ul>
        <li><b>P:</b> 49k-65k</li>
        <li><b>M:</b> 49k-63k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT short → D1</li>
        <li>ST short → D2</li>
        <li>ST Reprisal, H1 120s, H2 120s, D3</li>
      </ul>
    </td>
    <td>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Brightwing #3</p>
      <ul>
        <li><b>P:</b> 49k-65k</li>
        <li><b>M:</b> 49k-63k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Covered by ST <em>Reprisal</em>, H1 120s, H2 120s, D3</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Brightwing #4</p>
      <ul>
        <li><b>P:</b> 49k-65k</li>
        <li><b>M:</b> 49k-63k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT <em>Reprisal</em>, D4</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Covered by H1 120s, H2 120s, D3</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Pure of Heart</p>
      <ul>
        <li><b>P:</b> 61k-76k</li>
        <li><b>M:</b> 53k-64k</li>
      </ul>
    </td>
    <td></td>
    <td>
      <ul>
        <li>Covered by MT <em>Reprisal</em>, H1 120s, H2 120s, D4</li>
      </ul>
    </td>
  </tr>
</table>

### P5. Alternate Timeline Thordan

<table>
  <tr>
    <td>
      <p>Wrath of the Heavens</p>
      <ul>
        <li>H2 90s</li>
      </ul>
    </td>
    <td>
    </td>
    <td>
      <ul>
        <li>Strong shields are useful here because the party will be spread
        out.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Ancient Quaga #1</p>
      <ul>
        <li><b>P:</b> 85k-97k</li>
        <li><b>M:</b> 75k-93k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, MT 90s, H2 30s, D1, D3</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Notably, <em>Addle</em> is overkill here, and is better served at
        the second <em>Ancient Quaga</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Heavenly Heel → 3x Ascalon's Might #1</p>
      <ul>
        <li><b>T:</b> 242k-307k</li>
        <li><b>T:</b> 3x 84k-90k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><b>MT + ST:</b> Rampart + short</li>
        <li>ST Reprisal, D2</li>
      </ul>
    </td>
    <td>
      <li>A WAR should <em>Holmgang</em> instead.</li>
      <li>Tank swap if not taken by <em>Holmgang</em>.</li>
    </td>
  </tr>
  <tr>
    <td>
      <p>Death of the Heavens</p>
    </td>
    <td>
      <ul>
        <li>H1 120s, H2 120s</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>The damage from <em>Death of the Heavens</em> isn't lethal, but
        it's good to mitigate the damage to let the healers focus on the 
        mechanic. There also isn't any other good spot to use the healer 120s 
        mitigations.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Ancient Quaga #2</p>
      <ul>
        <li><b>P:</b> 85k-97k</li>
        <li><b>M:</b> 75k-93k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, ST 90s, H2 30s, D4</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Heavenly Heel → 3x Ascalon's Might #2</p>
      <ul>
        <li><b>T:</b> 175k-196k</li>
        <li><b>T:</b> 3x 84k-90k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>3rd + short</li>
        <li>ST Reprisal, D2, D3</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Tank swap MT→ST.</li>
        <li>Healers should help the tanks, as they cannot use their stronger 
        mitigations here.</li>
      </ul>
    </td>
  </tr>
</table>

### P6. Double Dragons

Notably, DRK is very strong in this phase because *Dark Mind* will be available
for both *Hallowed Wings*.

However, be careful if your party has DRK + SGE + SCH, as the healers will have
trouble topping up the DRK if *Living Dead* was used at *Cauterize*.

<table>
  <tr>
    <td>
      <p>Wyrmsbreath #1</p>
      <ul>
        <li><b>T:</b> 111k-144k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>30% + short</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>If only one mouth is glowing, the tank whose dragon's mouth glows
        can give their short mit to the other tank.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Akh Afah #1</p>
      <ul>
        <li><b>P:</b> 69k-76k</li>
        <li><b>M:</b> 65k-71k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT <em>Reprisal</em>, H2 30s</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>The MT needs to stand in the middle of the arena to hit
        <em>both</em> dragons with <em>Reprisal</em> before joining their
        <em>Akh Afah</em> stack.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Hallowed Wings #1</p>
      <ul>
        <li><b>T:</b> 121k-135k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><b>MT + ST:</b> <em>Rampart</em> + short</li>
        <li>ST <em>Reprisal</em></li>
      </ul>
    </td>
    <td>
      <ul>
        <li>The ST may not be able to <em>Reprisal</em> this in the event of
        tank downtime.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Wroth Flames</p>
      <ul>
        <li><b>P:</b> 4x 56k-62k</li>
        <li><b>M:</b> 4x 53k-60k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT 90s, ST 90s, H1 120s, H2 120s, D3, D4</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Add H2 30s if able- the latest H2 30s can be used and still be back
        for <em>Akh Afah</em> #2 is when the 2nd set of orbs spawn.</li>
        <li>WHM will typically use <em>Liturgy of the Bell</em> here.</li>
        <li>SGE will typically use <em>Panhaima</em> here.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Akh Afah #2</p>
      <ul>
        <li><b>P:</b> 69k-76k</li>
        <li><b>M:</b> 65k-71k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT <em>Reprisal</em>, H2 30s</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>The MT needs to stand in the middle of the arena to hit
        <em>both</em> dragons with <em>Reprisal</em> before joining their
        <em>Akh Afah</em> stack.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Hallowed Wings #2</p>
      <ul>
        <li><b>T:</b> 121k-135k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><b>MT + ST:</b> 3rd + short</li>
        <li>ST <em>Reprisal</em></li>
      </ul>
    </td>
    <td>
      <ul>
        <li>This set of <em>Hallowed Wings</em> hurt more because
        <em>Rampart</em> is not used. Furthermore, one tank will be on the 
        opposite side of the party (out of healing range). Additional 
        mitigation helps.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Wyrmsbreath #2</p>
      <ul>
        <li><b>T:</b> 111k-144k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><b>MT + ST:</b> <em>Rampart</em> + 30%</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>If timed correctly, tank mitigations can last until
        <em>Cauterize</em>.</li>
        <li>A tank's 25s short mitigation likely won't be available.</li>
        <li>A DRK will be able to use <em>The Blackest Night</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Cauterize</p>
      <ul>
        <li><b>T:</b> 217k-240k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Invuln</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>If <em>Wyrmsbreath</em> #2 was a single-target tankbuster, the tank
        that was <em>not</em> targeted can mitigate <em>Cauterize</em> instead
        to gain an invuln use at P7 (ideally at <em>Akh Morn's Edge #2</em>).
        A WAR should <em>Holmgang</em> regardless.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Alternative End</p>
      <ul>
        <li><b>P:</b> 116k-128k</li>
        <li><b>M:</b> 108k-120k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT 90s, ST 90s, H2 30s, H2 90s, D3</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>A SGE will need to add <em>Holos</em>.</li>
      </ul>
    </td>
  </tr>
</table>

### P7. Dragonking Thordan

Each hit from *Akh Morn's Edge* deals 36k-38k damage/second.

In contrast, each hit from *Gigaflare's Edge* deals 67k-71k base damage, but
the three hits are spaced out over 8 seconds, leading to an average of 25k-27k 
damage/second (this is somewhat made up for by having to move and heal).

<table>
  <tr>
    <td>
      <p>Akh Morn's Edge #1</p>
      <ul>
        <li><b>T:</b> 5x 63k-72k</li>
        <li><b>P:</b> 5x 36k-39k</li>
        <li><b>M:</b> 5x 33k-37k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><b>MT + ST:</b> <em>Rampart</em> + 3rd</li>
        <li>MT <em>Reprisal</em>, H1 120s, H2 30s, D1</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>If H2 30s is used right after the second <em>Trinity</em> 
        auto-attack after <em>Exaflare's Edge</em>, it will be available for
        <em>Gigaflare's Edge</em> #2.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Gigaflare's Edge #1</p>
      <ul>
        <li><b>P:</b> 3x 57k-69k</li>
        <li><b>M:</b> 3x 51k-67k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>ST <em>Reprisal</em>, D2, D4</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Akh Morn's Edge #2</p>
      <ul>
        <li><b>T:</b> 6x 63k-72k</li>
        <li><b>P:</b> 6x 36k-39k</li>
        <li><b>M:</b> 6x 33k-37k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><b>MT + ST:</b> 30%</li>
        <li>MT <em>Reprisal</em>, H1 180s, D3</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>If H2 30s is used right after the second <em>Trinity</em> 
        auto-attack after <em>Exaflare's Edge</em>, it will be available for
        <em>Gigaflare's Edge</em> #2.</li>
        <li>If MT 90s, ST 90s, D3 is used right after the second
        <em>Trinity</em> auto-attack after <em>Exaflare's Edge</em>, it will be 
        available for <em>Akh Morn's Edge</em> #3.</li>
        <li>A WAR should be careful about using <em>Shake It Off</em> here to
        avoid accidentally removing <em>Vengeance</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Gigaflare's Edge #2</p>
      <ul>
        <li><b>P:</b> 3x 57k-69k</li>
        <li><b>M:</b> 3x 51k-67k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>ST <em>Reprisal</em>, D1</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Akh Morn's Edge #3</p>
      <ul>
        <li><b>T:</b> 7x 63k-72k</li>
        <li><b>P:</b> 7x 36k-39k</li>
        <li><b>M:</b> 7x 33k-37k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><b>MT + ST:</b> <em>Rampart</em> + 3rd</li>
        <li>MT <em>Reprisal</em>, H1 120s, H2 30s, D2, D4</li>
      </ul>
    </td>
    <td></td>
  </tr>
</table>

## Mitigation by Role

### MT

<table>
  <tr>
    <td>
      <p><b>P2. Thordan</b></p>
    </td>
    <td>
      <p><b>3x Ascalon's Might</b></p>
      <ul>
        <li>short</li>
      </ul>
      <p><b>Strength of the Ward</b></p>
      <ul>
        <li>30%, short</li>
      </ul>
      <p><b>Ancient Quaga</b></p>
      <ul>
        <li>30%, short</li>
        <li>This is the latest you can use your MT 90s, and have it back by
        <em>Ultimate End</em></li>
      </ul>
      <p><b>Heavenly Heel</b></p>
      <ul>
        <li>Rampart + 3rd</li>
      </ul>
      <p><b>Ultimate End</b></p>
      <ul>
        <li><em>Reprisal</em>, MT 90s
          <ul>
            <li>A WAR/PLD can use <em>Shake It Off/Divine Veil</em> right after
            <em>Sanctity of the Ward</em> and get an additional use at the second
            <em>Eye of the Tyrant</em> stack, if killtime is slow enough.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P3. Nidhogg</b></p>
    </td>
    <td>
      <p><b>Eye of the Tyrant #2</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
      <p><b>Soul Tethers</b></p>
      <ul>
        <li>Invuln
          <ul>
            <li>The MT can mitigate the auto-attacks after <em>Soul
            Tethers</em>.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P4. Eyes + Saving Haurchefant</b></p>
    </td>
    <td>
      <p><b>Resentment</b></p>
      <ul>
        <li>Rampart → 30%</li>
        <li>MT 90s
          <ul>
            <li>This is just to help out with healing, as there is no other
            place to use it before saving Haurchefant.</li>
          </ul>
        </li>
      </ul>
      <p><b>Steep in Rage</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
      <p><b>Pure of Heart</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P5. Alternate Timeline Thordan</b></p>
    </td>
    <td>
      <p><b>Ancient Quaga</b></p>
      <ul>
        <li><em>Reprisal</em>, MT 90s</li>
        <li>Use your MT 90s early to have it back by the second <em>Ancient Quaga</em>.</li>
      </ul>
      <p><b>Heavenly Heel #1</b></p>
      <ul>
        <li><em>Rampart</em> + short</li>
        <li>A WAR can <em>Holmgang</em> instead. Tank swap if this wasn't taken with <em>Holmgang</em>.</li>
      </ul>
      <p><b>Ancient Quaga #2</b></p>
      <ul>
        <li>If you used your MT 90s early enough in the previous <em>Ancient Quaga</em>, it will be back up here.</li>
      </ul>
      <p><b>Heavenly Heel #2</b></p>
      <ul>
        <li>3rd + short</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P6. Double Dragons</b></p>
    </td>
    <td>
      <p><b>Wyrmsbreath #1</b></p>
      <ul>
        <li>30% + short</li>
        <li>If Hraesvelgr's mouth isn't glowing, use your short mitigation on
        the ST co-tank.</li>
      </ul>
      <p><b>Akh Afah #1</b></p>
      <ul>
        <li><em>Reprisal</em>
          <ul>
            <li>Stand in the middle of the arena to hit <em>both</em> dragons
            with <em>Reprisal</em> before joining the <em>Akh Afah</em>
            stack.</li>
          </ul>
        </li>
      </ul>
      <p><b>Hallowed Wings #1</b></p>
      <ul>
        <li><em>Rampart</em> + short</li>
      </ul>
      <p><b>Wroth Flames</b></p>
      <ul>
        <li>MT 90s</li>
      </ul>
      <p><b>Akh Afah #2</b></p>
      <ul>
        <li><em>Reprisal</em>
          <ul>
            <li>Stand in the middle of the arena to hit <em>both</em> dragons
            with <em>Reprisal</em> before joining the <em>Akh Afah</em>
            stack.</li>
          </ul>
        </li>
      </ul>
      <p><b>Hallowed Wings #2</b></p>
      <ul>
        <li>3rd + short</li>
      </ul>
      <p><b>Wyrmsbreath #2</b></p>
      <ul>
        <li>30% + <em>Rampart</em></li>
      </ul>
      <p><b>Cauterize</b></p>
      <ul>
        <li>Invuln</li>
      </ul>
      <p><b>Alternative End</b></p>
      <ul>
        <li>MT 90s</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><b>P7. Dragonking Thordan</b></td>
    <td>
      <p>ST 90s will be available from <em>Akh Morn's Edge</em> #2 onwards.</p>
      <p><b>Akh Morn's Edge #1</b></p>
      <ul>
        <li><em>Rampart + 3rd</em></li>
        <li><em>Reprisal</em></li>
      </ul>
      <p><b>Akh Morn's Edge #2</b></p>
      <ul>
        <li>30%</li>
        <li><em>Reprisal</em></li>
        <li>MT 90s used after the second auto-attack before <em>Akh Morn's
        Edge</em> #2, will get an additional use at <em>Akh Morn's
        Edge</em> #3.</li>
      </ul>
      <p><b>Akh Morn's Edge #3</b></p>
      <ul>
        <li><em>Rampart + 3rd</em></li>
        <li><em>Reprisal</em></li>
      </ul>
    </td>
  </tr>
</table>

### ST

<table>
  <tr>
    <td>
      <p><b>P2. Thordan</b></p>
    </td>
    <td>
      <p><b>3x Ascalon's Might</b></p>
      <ul>
        <li><em>Reprisal</em></li>
        <li>If the MT is a WAR, they'll be taking this with <em>Holmgang</em>.</li>
      </ul>
      <p><b>Strength of the Ward</b></p>
      <ul>
        <li>30%, short</li>
      </ul>
      <p><b>Heavenly Heel</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
      <p><b>3x Ascalon's Might</b></p>
      <ul>
        <li><em>Rampart</em> + short</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P3. Nidhogg</b></p>
    </td>
    <td>
      <p><b>Final Chorus</b></p>
      <ul>
        <li>ST 90s</li>
      </ul>
      <p><b>Eye of the Tyrant #1</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
      <p><b>Soul Tethers</b></p>
      <ul>
        <li>Invuln</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P4. Eyes + Saving Haurchefant</b></p>
    </td>
    <td>
      <p><b>Resentment</b></p>
      <ul>
        <li>Rampart → 30%</li>
        <li>ST 90s
          <ul>
            <li>This is just to help out with healing, as there is no other
            place to use it before saving Haurchefant.</li>
          </ul>
        </li>
      </ul>
      <p><b>Brightwing #2</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P5. Alternate Timeline Thordan</b></p>
    </td>
    <td>
      <p><b>Heavenly Heel #1</b></p>
      <ul>
        <li><em>Rampart</em> + short</li>
        <li><em>Reprisal</em></li>
        <li>A WAR MT will <em>Holmgang</em> this. Tank swap if this wasn't
        taken with <em>Holmgang</em>.</li>
      </ul>
      <p><b>Ancient Quaga #2</b></p>
      <ul>
        <li>If you used your MT 90s early enough in the previous
        <em>Ancient Quaga</em>, it will be back up here.</li>
      </ul>
      <p><b>Heavenly Heel #2</b></p>
      <ul>
        <li>3rd + short</li>
        <li><em>Reprisal</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P6. Double Dragons</b></p>
    </td>
    <td>
      <p><b>Wyrmsbreath #1</b></p>
      <ul>
        <li>30% + short
          <ul>
            <li>If Nidhogg's mouth isn't glowing, use your short mitigation
            on the MT.</li>
          </ul>
        </li>
      </ul>
      <p><b>Hallowed Wings #1</b></p>
      <ul>
        <li><em>Rampart</em> + short</li>
        <li>Reprisal
          <ul>
            <li>You may not be able to get this <em>Reprisal</em> if it's
            tank downtime.</li>
          </ul>
        </li>
      </ul>
      <p><b>Wroth Flames</b></p>
      <ul>
        <li>ST 90s</li>
      </ul>
      <p><b>Hallowed Wings #2</b></p>
      <ul>
        <li>3rd + short</li>
        <li><em>Reprisal</em></li>
      </ul>
      <p><b>Wyrmsbreath #2</b></p>
      <ul>
        <li>30% + <em>Rampart</em></li>
      </ul>
      <p><b>Cauterize</b></p>
      <ul>
        <li>Invuln</li>
      </ul>
      <p><b>Alternative End</b></p>
      <ul>
        <li>ST 90s</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><b>P7. Dragonking Thordan</b></td>
    <td>
      <p>ST 90s will be available from <em>Akh Morn's Edge</em> #2 onwards.</p>
      <p><b>Akh Morn's Edge #1</b></p>
      <ul>
        <li><em>Rampart + 3rd</em></li>
      </ul>
      <p><b>Gigaflare's Edge #1</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
      <p><b>Akh Morn's Edge #2</b></p>
      <ul>
        <li>30%</li>
        <li>ST 90s used after the second auto-attack before <em>Akh Morn's
        Edge</em> #2, will get an additional use at <em>Akh Morn's
        Edge</em> #3.</li>
      </ul>
      <p><b>Gigaflare's Edge #2</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
      <p><b>Akh Morn's Edge #3</b></p>
      <ul>
        <li><em>Rampart + 3rd</em></li>
      </ul>
    </td>
  </tr>
</table>

### H1

This assumes your H1 is either a WHM or AST. As double barrier healer parties
are fairly common, adapt this as needed if H1 is a SCH or SGE.

<table>
  <tr>
    <td>
      <p><b>P2. Thordan</b></p>
    </td>
    <td>
      <p>H1 120s mitigations are not commited anywhere in this phase. You can
      choose between:</p>
      <ul>
        <li><em>Strength of the Ward</em> + <em>Final Chorus</em></li>
        <li><em>Ancient Quaga</em> + <em>Heavenly Heel</em></li>
        <li><em>Sanctity of the Ward</em> + <em>Eye of the Tyrant</em> #2</li>
      </ul>
      <p><b>3x Ascalon's Might</b></p>
      <ul>
        <li><em>Aquaveil/Exaltation</em> → MT</li>
        <li>If the MT is a WAR, they'll be taking this with <em>Holmgang</em>.</li>
      </ul>
      <p><b>Sanctity of the Ward</b></p>
      <ul>
        <li>An AST's <em>Macrocosmos</em> is useful here, allowing an
        accidental 5-3 split to survive.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P3. Nidhogg</b></p>
    </td>
    <td>
      <p>H1 120s are not committed to any part of this phase, so feel free to
      use it for comfort.</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P4. Eyes + Saving Haurchefant</b></p>
    </td>
    <td>
      <p><b>Brightwing #2</b></p>
      <ul>
        <li>H1 120s
          <ul>
            <li>A WHM would <em>Liturgy of the Bell</em> here.</li>
          </ul>
        </li>
      </ul>
      <p>A WHM can use <em>Benediction</em> on Haurchefant.</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P5. Alternate Timeline Thordan</b></p>
    </td>
    <td>
      <p><b>Death of the Heavens</b></p>
      <ul>
        <li>H1 120s</li>
      </ul>
      <p><b>Heavenly Heel #2</b></p>
      <ul>
        <li><em>Aquaveil/Exaltation</em> → MT</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P6. Double Dragons</b></p>
    </td>
    <td>
      <p><b>Wroth Flames</b></p>
      <ul>
        <li>H1 120s</li>
        <li>A WHM would use <em>Liturgy of the Bell</em> here.</li>
      </ul>
      <p><b>Hallowed Wings #2</b></p>
      <ul>
        <li><em>Aquaveil/Exaltation</em> here on a tank is very nice.</li>
      </ul>
      <p><b>Cauterize</b></p>
      <ul>
        <li>An AST would use <em>Macrocosmos</em> here.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><b>P7. Dragonking Thordan</b></td>
    <td>
      <p><b>Akh Morn's Edge #1</b></p>
      <ul>
        <li>H1 120s</li>
      </ul>
      <p><b>Akh Morn's Edge #2</b></p>
      <ul>
        <li>H1 180s</li>
      </ul>
      <p><b>Akh Morn's Edge #3</b></p>
      <ul>
        <li>H1 120s</li>
      </ul>
    </td>
  </tr>
</table>

### H2

<table>
  <tr>
    <td>
      <p><b>P2. Thordan</b></p>
    </td>
    <td>
      <p>A SGE would prefer to <em>Holos</em> at <em>Strength of the Ward</em>,
      because <em>Sanctity of the Ward</em> can be covered by <em>Kerachole</em>
      + <em>Panhaima</em> (in addition to <em>Zoe</em> shields).</p>
      <p>A SGE may also need to hold <em>Holos</em> for <em>Final Chorus</em>,
      in which case they can use <em>Holos</em> only at <em>Strength of the
      Ward</em>.</p>
      <p><b>Ancient Quaga</b></p>
      <ul>
        <li>H2 30s</li>
      </ul>
      <p><b>Sanctity of the Ward</b></p>
      <ul>
        <li>H2 90s
          <ul>
            <li>Use this during the <em>Ascalon's Might</em> cleaves to ensure
            it will be back up in time for <em>Final Chorus</em>, even with
            faster killtimes.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P3. Nidhogg</b></p>
    </td>
    <td>
      <p><b>Final Chorus</b></p>
      <ul>
        <li>H2 30s, H2 90s
          <ul>
            <li>A SGE may need to add <em>Physis II</em> if no other extra
            mitigations are available.</li>
          </ul>
        </li>
      </ul>
      <p><b>Eye of the Tyrant #1</b></p>
      <ul>
        <li>H2 30s</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P4. Eyes + Saving Haurchefant</b></p>
    </td>
    <td>
      <p><b>Steep in Rage</b></p>
      <ul>
        <li>H2 30s</li>
      </ul>
      <p><b>Brightwing #2</b></p>
      <ul>
        <li>H2 120s</li>
        <li>A SGE would use <em>Panhaima</em> here.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P5. Alternate Timeline Thordan</b></p>
    </td>
    <td>
      <p><b>Wrath of the Heavens</b></p>
      <ul>
        <li>H2 90s</li>
      </ul>
      <p><b>Ancient Quaga #1</b></p>
      <ul>
        <li>H2 30s</li>
      </ul>
      <p><b>Death of the Heavens</b></p>
      <ul>
        <li>H2 120s</li>
      </ul>
      <p><b>Ancient Quaga #2</b></p>
      <ul>
        <li>H2 30s</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P6. Double Dragons</b></p>
    </td>
    <td>
      <p><b>Wyrmsbreath #1</b></p>
      <ul>
        <li>H2 90s
          <ul>
            <li>A SGE can catch this with a <em>Kerachole</em> (and have it
            back for <em>Akh Afah</em>) if <em>Kerachole</em> is used right
            after the second GCD.</li>
          </ul>
        </li>
      </ul>
      <p><b>Akh Afah #1</b></p>
      <ul>
        <li>H2 30s</li>
      </ul>
      <p><b>Wroth Flames</b></p>
      <ul>
        <li>H2 120s
          <li>A SGE would <em>Panhaima</em> here.</li>
        </li>
      </ul>
      <p><b>Hallowed Wings #2</b></p>
      <ul>
        <li>The tanks are taking more damage here, so give them more attention.</li>
      </ul>
      <p><b>Alternative End</b></p>
      <ul>
        <li>H2 30s, H2 90s
          <li>A SGE will need to add <em>Holos</em>.</li>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><b>P7. Dragonking Thordan</b></td>
    <td>
      <p>Notably, SCH would prefer to use <em>Seraph</em> at <em>Gigaflare's
      Edge</em>, while a SGE's <em>Panhaima</em> excels at <em>Akh Morn's
      Edge</em> #1 and #3, so use <em>Expedient/Holos</em> to fill in as
      needed, as the mitigation plan does not specify any particular place for
      the H2 120s mitigations.</p>
      <p><b>Akh Morn's Edge #1</b></p>
      <ul>
        <li>H2 30s
          <ul>
            <li>Use the H2 30s right after the second auto-attack following
            <em>Exaflare's Edge</em> to get an additional use at <em>Gigaflare's
            Edge</em> #1.</li>
          </ul>
        </li>
      </ul>
      <p><b>Akh Morn's Edge #2</b></p>
      <ul>
        <li>H2 30s
          <ul>
            <li>Use the H2 30s right after the second auto-attack following
            <em>Exaflare's Edge</em> to get an additional use at <em>Gigaflare's
            Edge</em> #2.</li>
          </ul>
        </li>
      </ul>
      <p><b>Akh Morn's Edge #3</b></p>
      <ul>
        <li><em>H2 30s</em></li>
      </ul>
    </td>
  </tr>
</table>

### D1

<table>
  <tr>
    <td>
      <p><b>P2. Thordan</b></p>
    </td>
    <td>
      <p><b>3x Ascalon's Might</b></p>
      <ul>
        <li><em>Feint</em>
          <ul>
            <li>A WAR will <em>Holmgang</em> this.</li>
          </ul>
        </li>
      </ul>
      <p><b>Ultimate End</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P3. Nidhogg</b></p>
    </td>
    <td>
      <p><em>Feint</em> doesn't change any breakpoints in this phase, so feel
      free to use it as you please.</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P4. Eyes + Saving Haurchefant</b></p>
    </td>
    <td>
      <p><b>Brightwing #2</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P5. Alternate Timeline Thordan</b></p>
    </td>
    <td>
      <p><b>Ancient Quaga #1</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
      <p><b>Heavenly Heel #2</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><b>P6. Double Dragons</b></td>
    <td>
      <p>There aren't any great places to <em>Feint</em>. To just help out,
      the best places would either be <em>Wroth Flames</em>, or
      <em>Hallowed Wings</em> #2.</p>
    </td>
  </tr>
  <tr>
    <td><b>P7. Dragonking Thordan</b></td>
    <td>
      <p><b>Akh Morn's Edge #1</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
      <p><b>Gigaflare's Edge #2</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
    </td>
  </tr>
</table>

### D2

This assumes D2 is a melee DPS.

<table>
  <tr>
    <td>
      <p><b>P2. Thordan</b></p>
    </td>
    <td>
      <p><b>Heavenly Heel</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P3. Nidhogg</b></p>
    </td>
    <td>
      <p><b>Eye of the Tyrant #2</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P4. Eyes + Saving Haurchefant</b></p>
    </td>
    <td>
      <p><b>Brightwing #4</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P5. Alternate Timeline Thordan</b></p>
    </td>
    <td>
      <p><b>Heavenly Heel #1</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><b>P6. Double Dragons</b></td>
    <td>
      <p>There aren't any great places to <em>Feint</em>. To just help out,
      the best places would either be <em>Wroth Flames</em>, or
      <em>Hallowed Wings</em> #2.</p>
    </td>
  </tr>
  <tr>
    <td><b>P7. Dragonking Thordan</b></td>
    <td>
      <p><b>Gigaflare's Edge #1</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
      <p><b>Akh Morn's Edge #3</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
    </td>
  </tr>
</table>

### D3

<table>
  <tr>
    <td>
      <p><b>P2. Thordan</b></p>
    </td>
    <td>
      <p><b>Strength of the Ward</b></p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P3. Nidhogg</b></p>
    </td>
    <td>
      <p><b>Final Chorus</b></p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P4. Eyes + Saving Haurchefant</b></p>
    </td>
    <td>
      <p><b>Hatebound</b></p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em></li>
      </ul>
      <p><b>Brightwing #2</b></p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P5. Alternate Timeline Thordan</b></p>
    </td>
    <td>
      <p><b>Ancient Quaga #1</b></p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em></li>
      </ul>
      <p><b>Heavenly Heel #2 → 3x Ascalon's Might</b></p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P6. Double Dragons</b></p>
    </td>
    <td>
      <p>The best places for a MCH to use <em>Dismantle</em> would either be at
      <em>Wroth Flames</em>, or at <em>Hallowed Wings</em> #2 (use
      <em>Dismantle</em> on Hraesvelgr).</p>
      <p><b>Wroth Flames</b></p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em></li>
      </ul>
      <p><b>Alternative End</b></p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em>
          <ul>
            <li>A DNC can extract the maximum value from <em>Improvised
            Finish</em> if they start <em>Improvisation</em> when Thordan's
            dialogue box disappears.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><b>P7. Dragonking Thordan</b></td>
    <td>
      <p><b>Akh Morn's Edge #2</b></p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em>
          <ul>
            <li>If used after the second auto-attack before <em>Akh Morn's
            Edge</em> #2, you can get an additional use at <em>Akh Morn's
            Edge</em> #3.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
</table>

### D4

<table>
  <tr>
    <td>
      <p><b>P2. Thordan</b></p>
    </td>
    <td>
      <p><b>Ancient Quaga</b></p>
      <ul>
        <li><em>Addle</em></li>
      </ul>
      <p><b>Ultimate End</b></p>
      <ul>
        <li><em>Addle</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P4. Eyes + Saving Haurchefant</b></p>
    </td>
    <td>
      <p><b>Brightwing #4</b></p>
      <ul>
        <li><em>Addle</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P5. Alternate Timeline Thordan</b></p>
    </td>
    <td>
      <p><b>Ancient Quaga #2</b></p>
      <ul>
        <li><em>Addle</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P6. Double Dragons</b></p>
    </td>
    <td>
      <p><b>Wroth Flames</b></p>
      <ul>
        <li><em>Addle</em>
          <ul>
            <li>Nidhogg will start out of range if it's the downtime
            pattern. You can also use <em>Addle</em> at <em>Hallowed
            Wings</em> #2 instead (on Hraesvelgr).</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><b>P7. Dragonking Thordan</b></td>
    <td>
      <p><b>Gigaflare's Edge #1</b></p>
      <ul>
        <li><em>Addle</em></li>
      </ul>
      <p><b>Akh Morn's Edge #3</b></p>
      <ul>
        <li><em>Addle</em></li>
      </ul>
    </td>
  </tr>
</table>
