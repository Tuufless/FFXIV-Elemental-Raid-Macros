---
layout: default
title: Mitigation
parent: Lv 90. TOP
nav_order: 9
has_children: false
has_toc: false
grand_parent: Ultimates
permalink: /ultimates/top/mitigation/
---

# Mitigation

The following is a mitigation framework for the encounter.

It is *not* a plan for every single cooldown available to the party; instead,
think of the following as a bare-bones framework to work with- i.e: these are
the things that people will generally look for when mitigation is missing.

<table>
  <th>Mitigation by Phase</th>
  <tr>
    <td>
      <ul>
        <li><a href="#p1-omega">P1. Omega</a></li>
        <li><a href="#p2-omega-mf">P2. Omega-M/F</a></li>
        <li><a href="#p3-omega-reconfigured">P3. Omega Reconfigured</a></li>
        <li><a href="#p4-blue-screen">P4. Blue Screen</a></li>
        <li><a href="#p5-run-dynamis">P5. Run Dynamis</a></li>
        <li><a href="#p6-alpha-omega">P6. Alpha Omega</a></li>
      </ul>
    </td>
  </tr>
</table>

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
  The raw damage values have also been provided, separated into damage dealt
  to <b>T</b>anks (MT, ST), <b>P</b>hysical DPS (D1, D2, D3), and <b>M</b>agic 
  (H1, H2, D4).
</div>

Physical DPS jobs have higher max HP, but lower magic defense compared to
casters.

- Tanks have 110k max HP.
- Physical DPS jobs have 77k max HP.
- Magical jobs have 68k max HP.
- Basic shields *(Succor, Eukrasian Prognosis)* absorb 8k damage.

<details markdown=block>
<summary>
  <b>Legend</b>
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

## Mitigation by Phase

### P1. Omega

Party mitigation should be used anytime by the second Condensed Wave during 
Pantokrator. There are 6 seconds between each wave, so all tank and healer
mitigations can cover at least three waves each.

They will be comfortably back in time for their next use in P2.

<table>
  <tr>
    <td>
      <p>Condensed Wave #1</p>
      <ul>
        <li><b>P:</b> 50k-67k</li>
        <li><b>M:</b> 46k-63k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT Reprisal</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Condensed Wave #2</p>
      <ul>
        <li><b>P:</b> 50k-67k</li>
        <li><b>M:</b> 46k-63k</li>
      </ul>
    </td>
    <td></td>
    <td>
      <ul>
        <li>Covered by MT Reprisal.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Condensed Wave #3</p>
      <ul>
        <li><b>P:</b> 50k-67k</li>
        <li><b>M:</b> 46k-63k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>ST Reprisal</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Condensed Wave #4</p>
      <ul>
        <li><b>P:</b> 50k-67k</li>
        <li><b>M:</b> 46k-63k</li>
      </ul>
    </td>
    <td></td>
    <td>
      <ul>
        <li>Covered by ST Reprisal.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Pantokrator (Diffuse Wave Cannon Kyrios)</p>
    </td>
    <td>
      <ul>
        <li><b>MT + ST:</b> Invuln</li>
      </ul>
    </td>
    <td></td>
  </tr>
</table>

### P2. Omega-M/F

Healer 120s mitigations will be needed to mitigate Pile Pitch + Meteors.
However, the problem is that we also need them to be available for the second
set of towers in P3- if the party does not hold DPS in P2, there is a chance
that the healer 120s won't come off cooldown in time.

- One option is to use the healer 120s to mitigate Optimized Bladedance (the 
  tethers) and Meteors.
  - The healer 120s will be back up comfortably in time for the 2nd set of
    towers in P3.
  - Lets the tanks survive Optimized Bladedance without *Rampart*, in the event
    they did not pop it early at the at the start of the phase.
  - The healer 120s will *not* cover *Cosmo Memory*.
- Alternatively, the earliest you can use the healer 120s and still cover
  *Cosmo Memory* is when the Flare markers appear.

Targeted mitigations, like *Addle*, *Feint*, and *Reprisal* have minimal use in 
this phase as the hard-hitting raid-wide damage comes from non-targetable
sources. As such, debuffs are better used on Omega-M/F's autoattacks.

<table>
  <tr>
    <td>
      <p>Solar Ray</p>
      <ul>
        <li><b>T:</b> 170-198k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Rampart, short</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Use Rampart when Omega becomes untargetable in the previous phase.</li>
        <li>A DRK should also Dark Mind.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Optimized Bladedance</p>
      <ul>
        <li><b>T:</b> 182k-231k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Rampart, 30%, 3rd, short</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Dark Mind will not work, as this is physical damage.</li>
        <li>Healer 120s can be used to help the tanks mitigate in the
        event they don't have <em>Rampart</em>, and guarantee that they will
        be available for 2nd towers in P3, but they will not cover <em>Cosmo 
        Memory</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>Pile Pitch + Meteors</td>
    <td>
      <ul>
        <li>MT 90s, ST 90s, H1 120s, H2 120s, H2 30s, D3</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>The earliest you can use the healer 120s and still catch
        <em>Cosmo Memory</em> is when the Flare markers appear.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td rowspan="2">
      <p>Cosmo Memory</p>
      <ul>
        <li><b>P:</b> 85k-104k</li>
        <li><b>M:</b> 76k-96k</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <ul>
        <li>This is also covered by H2 30s and D3 from Pile Pitch + Meteors,
        and possibly the healer 120s depending on when they were used.</li>
        <li>Any "extra" mitigations <em>(Magick Barrier, Passage of Arms, etc.)</em> should be used here.</li>
      </ul>
    </td>
  </tr>
</table>

### P3. Omega Reconfigured

- The party needs at least three pieces of 10% mitigation (shields count) to
  survive each round of towers and tethers *without* any healing in between.
- You can get 3-4 uses of H2 30s mitigations, depending on whether you use an
  H2 30s mitigation early at *Hello, World*.
- Tanks should mitigate Omega's autoattacks between each set of towers. Some
  groups may opt to tank swap after the second tower to cycle through both
  tank's cooldowns.

<table>
  <tr>
    <td>
      <p>Hello, World</p>
      <ul>
        <li><b>P:</b> 74k-82k</li>
        <li><b>M:</b> 68k-76k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, D1, D4</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Towers #1</p>
      <ul>
        <li><b>P:</b> 89k-98k</li>
        <li><b>M:</b> 74k-93k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT 90s, ST Reprisal</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>A WAR/PLD can use <em>Shake It Off/Divine Veil</em> early here to
        get an extra use at <em>Critical Error</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Towers #2</p>
      <ul>
        <li><b>P:</b> 89k-98k</li>
        <li><b>M:</b> 74k-93k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>H1 120s, H2 120s</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>This is the latest you can use healer 120s for them to be back in
        time for P4.</li>
        <li>Depending on when the healer 120s were using in P2, and the P2
        killtime, they may not be up in time to catch the full sequence, in 
        which case healers may need to heal in between tethers.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Towers #3</p>
      <ul>
        <li><b>P:</b> 89k-98k</li>
        <li><b>M:</b> 74k-93k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, ST 90s</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Towers #4</p>
      <ul>
        <li><b>P:</b> 89k-98k</li>
        <li><b>M:</b> 74k-93k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>ST Reprisal, D3</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Critical Error</p>
      <ul>
        <li><b>P:</b> 88k-97k</li>
        <li><b>M:</b> 81k-90k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>D1, D4</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><em>Critical Error</em> needs an additional H2 30s, <em>or</em> H2
        90s to guarantee survival.</li>
        <li>Any "extra" mitigations <em>(Magick Barrier, Passage of Arms, 
        etc.)</em> should be used here.</li>
      </ul>
    </td>
  </tr>
</table>

### P4. Blue Screen

- Because the Tank 90s, D1, and D3 mitigations are being saved for *Run
  Dynamis (Delta Version)*, they *cannot* be used in this phase.
- Only the healers and D4 will be mitigating this phase (with some support
  from *Reprisal*). Where they are used does not particularly matter, so they
  have *not* been included below.
  - Each healer 120s will last two stacks and two spreads.
  - Tanks will use *Reprisal* on the first two sets of Wave Cannons.

<table>
  <tr>
    <td>
      <p>Wave Cannon #1 (spread)</p>
      <ul>
        <li><b>P:</b> 29k-41k</li>
        <li><b>M:</b> 27k-37k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT Reprisal</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Wave Cannon #1 (stack)</p>
      <ul>
        <li><b>P:</b> 46k-58k</li>
        <li><b>M:</b> 42k-55k</li>
      </ul>
    </td>
    <td></td>
    <td>
      <ul>
        <li>Covered by the MT Reprisal.</li>
        <li>A SCH's <em>Expedient</em> is particularly useful here.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Wave Cannon #2 (spread)</p>
      <ul>
        <li><b>P:</b> 29k-41k</li>
        <li><b>M:</b> 27k-37k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>ST Reprisal</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Wave Cannon #2 (stack)</p>
      <ul>
        <li><b>P:</b> 46k-58k</li>
        <li><b>M:</b> 42k-55k</li>
      </ul>
    </td>
    <td></td>
    <td>
      <ul>
        <li>Covered by the ST Reprisal.</li>
        <li>This is the latest you can use H2 30s mitigations and have them
        back by <em>Blue Screen</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Wave Cannon #3 (spread)</p>
      <ul>
        <li><b>P:</b> 29k-41k</li>
        <li><b>M:</b> 27k-37k</li>
      </ul>
    </td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Wave Cannon #3 (stack)</p>
      <ul>
        <li><b>P:</b> 46k-58k</li>
        <li><b>M:</b> 42k-55k</li>
      </ul>
    </td>
    <td></td>
    <td>
      <ul>
        <li>Healer 120s mitigations used here will also cover <em>Blue
        Screen</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Blue Screen</p>
      <ul>
        <li><b>P:</b> 71k-81k</li>
        <li><b>M:</b> 69k-76k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>H2 30s</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>H2 120s can be used to substitute for shields or H2 30s.</li>
      </ul>
    </td>
  </tr>
</table>

### P5. Run Dynamis

There are a number of details when it comes to mitigating this phase:

- How the party handles *Solar Ray* will largely depend on whether a WAR is in
  the party.
  - If you have a WAR, then both tanks will be able to use all their personal 
    cooldowns to mitigate *Solar Ray* without additional help.
  - If you do *not* have a WAR, then the tanks will need to alternate between
    who uses their 30%. The tank that does not will need *Reprisal* and two other 
    10% mitigations from the healers and/or D4 to survive.
- Each Run Dynamis needs both tank 90s, H2 30s, D3's party mitigation,
  *Reprisal*, *Feint*, and shields to survive.
  - It is expected that all tanks + D3 use their 90s mitigations when the
    second *Solar Ray* hit lands just before Run Dynamis (Delta Version). This
    will catch Run Dynamis (Delta Version) at the tail end, and be back off
    cooldown in time for Run Dynamis (Sigma Version).
  - A single player cannot *Feint* all three *Run Dynamis*, hence why we
    alternate between D1 and D2's *Feint*.
- *Reprisal* will be available for each *Solar Ray* and *Run Dynamis*. However,
  if the tanks are going to mitigate *Solar Ray*, the MT should use their 
  *Reprisal* on *Solar Ray*, leaving the ST to *Reprisal* the *Run Dynamis*.
- Healer mitigations and D4's *Addle* are free to be used wherever appropriate.

<table>
  <tr>
    <td>
      <p>Solar Ray #1</p>
      <ul>
        <li><b>T:</b> 242k-307k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Hallowed Ground > Superbolide > full mits + swap</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Run Dynamis (Delta Version)</p>
      <ul>
        <li><b>P:</b> 131k-145k</li>
        <li><b>M:</b> 122k-135k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT 90s, ST Reprisal, ST 90s, H2 30s, D1, D3</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT 90s, ST 90s, D3 should be used at the second Solar Ray
        hit for them to be back for <em>Run Dynamis (Sigma Version)</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Solar Ray #2</p>
      <ul>
        <li><b>T:</b> 242k-307k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Superbolide > Living Dead > full mits + swap</li>
        <li>MT Reprisal</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Run Dynamis (Sigma Version)</p>
      <ul>
        <li><b>P:</b> 131k-145k</li>
        <li><b>M:</b> 122k-135k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT 90s, ST Reprisal, ST 90s, H2 30s, D2, D3</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Solar Ray #3</p>
      <ul>
        <li><b>T:</b> 242k-307k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>
          <p>Holmgang > mitigate + swap</p>
          <p>If no WAR:</p>
          <ul>
            <li><b>MT:</b> Rampart + 3rd + short</li>
            <li><b>ST:</b> 30% + Rampart + short</li>
          </ul>
        </li>
        <li>MT Reprisal</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>If this is not taken by <em>Holmgang</em>, both tanks will need to
        pop <em>Rampart</em> when the arm lasers resolve.</li>
        <li>Healers help the MT with mitigation.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Run Dynamis (Omega Version)</p>
      <ul>
        <li><b>P:</b> 131k-145k</li>
        <li><b>M:</b> 122k-135k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT 90s, ST Reprisal, ST 90s, H2 30s, D1, D3</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Solar Ray #4</p>
      <ul>
        <li><b>T:</b> 242k-307k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><p>Mitigate + swap</p>
          <p>If no WAR:</p>
          <ul>
            <li><b>MT:</b> 30% + Rampart + short</li>
            <li><b>ST:</b> Rampart + 3rd + short</li>
          </ul>
        </li>
        <li>MT Reprisal</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Healers help the ST with mitigation.</li>
        <li>If H1 uses their 120s here, it will be back up just in time for 
        <em>Cosmo Dive</em> in P6.</li>
      </ul>
    </td>
  </tr>
</table>

### P6. Alpha Omega

There isn't too much wiggle room in this phase given how hard everything hits,
however, there are still some points worth mentioning.

- *Feint* does not actually change any breakpoints in the worst case scenario,
  so its inclusion is just for comfort. It makes a small difference at
  *Cosmo Meteor's* Flares, where a *Feint* with a *Zoe* ensures survival even
  with high rolls.
- Be careful about applying debuffs on the boss during *Wave Cannon's* spreads,
  for you risk not having LB3 at *Cosmo Dive* 2.

<table>
  <tr>
    <td>
      <p>Cosmo Memory</p>
      <p><em>(after tank LB3)</em></p>
      <ul>
        <li><b>P:</b> 74k-82k</li>
        <li><b>M:</b> 69k-76k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT90s, ST Reprisal, H2 30s, D1</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><b>Tank LB:</b> WAR > PLD > DRK > GNB</li>
        <li>The party actually just needs one piece of mitigation to survive
        Cosmo Memory after the Tank LB3- the other mitigations are to put them
        on cooldown so they are not accidentally used elsewhere, and to reduce
        the amount of healing needed to top the party back up.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Cosmo Dive #1</p>
      <ul>
        <li><b>T:</b> 235k-286k</li>
        <li><b>P:</b> 94k-104k</li>
        <li><b>M:</b> 87k-96k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT + ST Rampart + 3rd + short</li>
        <li>MT Reprisal, H1 120s, H2 30s, D4</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Wave Cannon #1 (spread)</p>
      <ul>
        <li><b>P:</b> 84k-93k</li>
        <li><b>M:</b> 78k-86k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>H2 30s, D3</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Wave Cannon #1 (stack)</p>
      <ul>
        <li><b>T:</b> 315k-370k</li>
        <li><b>P:</b> 102k-119k</li>
        <li><b>M:</b> 94k-110k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><b>MT:</b> 30% + short</li>
        <li><b>ST:</b> Invuln + give short to MT</li>
        <li>ST Reprisal, ST 90s, D2</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Also covered by H2 30s and D3.</li>
        <li>If the ST is a DRK or GNB, they can use their 90s to mitigate
        <em>Wave Cannon</em>'s spreads.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Wave Cannon #2 (spread)</p>
      <ul>
        <li><b>P:</b> 84k-93k</li>
        <li><b>M:</b> 78k-86k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>H2 30s, H2 120s</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Wave Cannon #2 (stack)</p>
      <ul>
        <li><b>T:</b> 315k-370k</li>
        <li><b>P:</b> 102k-119k</li>
        <li><b>M:</b> 94k-110k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><b>MT:</b> Invuln + give short to ST</li>
        <li><b>ST:</b> 30% + short</li>
        <li>MT Reprisal, MT 90s, D1</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Also covered by H2 30s and H2 120s.</li>
        <li>If the MT is a DRK or GNB, they can use their 90s to mitigate
        <em>Wave Cannon</em>'s spreads.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Cosmo Dive #2</p>
      <ul>
        <li><b>T:</b> 235k-286k</li>
        <li><b>P:</b> 94k-104k</li>
        <li><b>M:</b> 87k-96k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Rampart + 3rd + short</li>
        <li>MT Reprisal, H1 120s, H2 30s, D2, D4</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Cosmo Meteor (Meteors)</p>
      <ul>
        <li><b>P:</b> 101k-112k</li>
        <li><b>M:</b> 94k-106k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, ST 90s, H1 120s, H2 30s, D3</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Cosmo Meteor (Flares)</p>
      <ul>
        <li><b>P:</b> 73k-90k</li>
        <li><b>M:</b> 64k-85k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>H2 90s, D2</li>
      </ul>
    </td>
    <td></td>
  </tr>
</table>
