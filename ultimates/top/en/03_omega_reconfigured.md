---
layout: default
title: 3. Omega Reconfigured
parent: Lv 90. TOP
grand_parent: Ultimates
permalink: /ultimates/top/03_omega_reconfigured/
---

# Omega Reconfigured

<div style="background-color: #200 ; padding: 10px; border: 1px solid;">
<b>UNDER CONSTRUCTION!</b>
</div>

## Transition

<div style="background-color: #200 ; padding: 10px; border: 1px solid;">
<b>UNDER CONSTRUCTION!</b>
</div>

## Hello, World

Although Hello, World may look overwhelming at first, it is simply a cycle of debuffs to resolve. At any one point, two players will be at each stage in the cycle.

<table>
  <tr>
    <td><p>The basic loop consists of:</p>
    <ol>
      <li>Orientate to coloured towers.</li>
      <li>Pair players together:
        <ul>
          <li>Critical Overflows pair with Local Regression (red/green).</li>
          <li>Critical Synchronizations pair with Remote Regression (blue).</li>
        </ul>
      </li>
      <li>Critical Overflows and Critical Synchronizations resolve.</li>
      <li>Pass Critical Underflow and Critical Performance. Break Remote Regression (blue) tethers.</li>
      <li>Break Local Regression (red/green) tethers.</li>
      <li>Repeat the loop with the next mechanic in the cycle.<ul><em>If you just took a tower, you will swap sides/colours for the next iteration.</em></ul></li>
    </ol></td>
    <td><img src="../images/03_omega_reconfigured/hello_world_cycle.jpg"></td>
  </tr>
</table>

The only variation is which colour each debuffs go to, which is determined by which colour debuff (Critical Performance and Critical Underflow) get paired with Critical Overflow and Critical Synchronization.

This loop is repeated four times (so all players will have their go at each debuff), although the final iteration has one small difference where the Local Regression players stand away from the Critical Overflows instead.

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
<details markdown=block>
<summary><b>[Click to Expand] Hello, World debuffs</b></summary>
<table>
  <tr>
    <td><img src="../images/03_omega_reconfigured/debuffs/latent_synchronization_bug.png"></td>
    <td><p><b>Latent Synchronization Bug</b></p><ul><li>This is a 70s debuff that will kill the player if left to timeout.</li><li>This is cleansed by taking damage from a Critical Synchronization Bug.</li></ul></td>
  </tr>
  <tr>
    <td><img src="../images/03_omega_reconfigured/debuffs/local_code_smell.png"><img src="../images/03_omega_reconfigured/debuffs/local_regression.png"></td>
    <td><p><b>Local Code Smell</b></p><ul><li>All players will get this debuff in pairs of 24s, 44s, 64s, and 84s.</li><li>The duration will always be 40 seconds off from the player's Remote Code Smell debuff.</li><li>As the timer approaches zero, emphemeral red+green tethers will connect the two players.</li><li>When the timer expires, the tethers activate and turn into Local Regression.</li></ul>
    <p><b>Local Regression</b></p><ul><li>When the two players move <b>near</b> one another, the tether "breaks", dealing magical damage to the party, applying a stack of Magic Vulnerability Up, and a stack of Thrice-come Ruin that only lasts for a second.</li></ul></td>
  </tr>
  <tr>
    <td><img src="../images/03_omega_reconfigured/debuffs/remote_code_smell.png"><img src="../images/03_omega_reconfigured/debuffs/remote_regression.png"></td>
    <td><p><b>Remote Code Smell</b></p><ul><li>All players will get this debuff in pairs of 24s, 44s, 64s, and 84s.</li><li>The duration will always be 40 seconds off from the player's Local Code Smell debuff.</li><li>As the timer approaches zero, emphemeral blue tethers will connect the two players.</li><li>When the timer expires, the tethers activate and turn into Remote Regression.</li></ul>
    <p><b>Remote Regression</b></p><ul><li>When the two players move <b>away</b> from one another, the tether "breaks", dealing magical damage to the party, applying a stack of Magic Vulnerability Up, and a stack of Thrice-come Ruin that only lasts for a second.</li></ul></td>
  </tr>
  <tr>
    <td><img src="../images/03_omega_reconfigured/debuffs/cascading_latent_defect.png"><img src="../images/03_omega_reconfigured/debuffs/latent_performance_defect.png"></td>
    <td><p><b>Cascading Latent Defect</b></p>
    <ul><li>Standing inside a red tower when the tower resolves will apply this debuff.</li>
    <li>This debuff will kill the player when the timer expires.</li>
    <li>It is cleansed when that player's Critical Underflow Bug expires. Players must have the Critical Underflow Bug <b>before</b> taking a red tower.</li></ul>
    <p><b>Latent Performance Defect</b></p>
    <ul><li>Standing inside a blue tower when the tower resolves will apply this debuff.</li><li>This debuff will kill the player when the timer expires.</li><li>It is cleansed when that player's Critical Performance Bug expires. Players must have the Critical Performance Bug <b>before</b> taking a blue tower.</li></ul></td>
  </tr>
  <tr>
    <td><img src="../images/03_omega_reconfigured/debuffs/overflow_code_smell.png"><img src="../images/03_omega_reconfigured/debuffs/critical_overflow_bug.png"><img src="../images/03_omega_reconfigured/debuffs/overflow_debugger.png"></td>
    <td><p><b>Overflow Code Smell</b></p><ul><li>This is a 3 second debuff that acts as a grace period.</li><li>When the debuff expires, it turns into a Critical Overflow Bug.</li></ul><p><b>Critical Overflow Bug</b></p><ul><li>This debuff is often nicknamed "Defamation".</li><li>When the timer expires, a giant AoE (roughly the same size as the arena) centered on the player goes off.</li><li>Any players hit by this AoE get a fresh Critical Overflow Bug.</li><li>When the debuff expires, it turns into an Overflow Debugger buff.</li></ul><p><b>Overflow Debugger</b></p><ul><li>Blocks the player from receiving one instance of Critical Overflow.</li></ul></td>
  </tr>
  <tr>
    <td><img src="../images/03_omega_reconfigured/debuffs/synchronization_code_smell.png"><img src="../images/03_omega_reconfigured/debuffs/critical_synchronization_bug.png"><img src="../images/03_omega_reconfigured/debuffs/synchronization_debugger.png"></td>
    <td><p><b>Synchronization Code Smell</b></p><ul><li>This is a 3 second debuff that acts as a grace period.</li><li>When the debuff expires, it turns into a Critical Synchronization Bug.</li></ul><p><b>Critical Synchronization Bug</b></p><ul><li>When the timer expires, an AoE (roughly the same size as a tower) centered on the player goes off that is divided between all players hit.</li><li>This AoE should be shared with one other player.</li><li>Any players hit by this AoE get a fresh Critical Synchronization Bug.</li><li>When the debuff expires, it turns into an Synchronization Debugger buff.</li></ul><p><b>Synchronization Debugger</b></p><ul><li>Blocks the player from receiving one instance of Critical Synchronization.</li></ul></td>
  </tr>
  <tr>
    <td><img src="../images/03_omega_reconfigured/debuffs/underflow_code_smell.png"><img src="../images/03_omega_reconfigured/debuffs/critical_underflow_bug.png"><img src="../images/03_omega_reconfigured/debuffs/underflow_debugger.png"></td>
    <td>
      <p><b>Underflow Code Smell</b></p>
      <ul>
        <li>This is a 3 second debuff that acts as a grace period.</li>
        <li>When the debuff expires, it turns into a Critical Underflow Bug.</li>
      </ul>
      <p><b>Critical Underflow Bug</b></p>
      <ul>
        <li>This is often nicknamed as the "red Nisi".</li>
        <li>This debuff is required to cleanse the Cascading Latent Defect debuff gained as a result of taking a red tower.</li>
        <li>When the timer expires, an AoE (roughly the same size as a tower) centered on the player goes off and will kill any other player hit.</li>
        <li>While the debuff is active, it can be passed to other players by touching them.</li>
        <li>When passed, the player gains a Underflow Debugger buff.</li>
      </ul>
      <p><b>Underflow Debugger</b></p>
      <ul><li>Prevents the player from receiving a Critical Underflow Bug.</li></ul></td>
  </tr>
  <tr>
    <td><img src="../images/03_omega_reconfigured/debuffs/performance_code_smell.png"><img src="../images/03_omega_reconfigured/debuffs/critical_performance_bug.png"><img src="../images/03_omega_reconfigured/debuffs/performance_debugger.png"></td>
    <td><p><b>Performance Code Smell</b></p>
    <ul>
      <li>This is a 3 second debuff that acts as a grace period.</li>
      <li>When the debuff expires, it turns into a Critical Performance Bug.</li>
    </ul>
    <p><b>Critical Performance Bug</b></p>
    <ul>
      <li>This is often nicknamed as the "blue Nisi".</li>
      <li>This debuff is required to cleanse the Cascading Latent Defect debuff gained as a result of taking a blue tower.</li>
      <li>When the timer expires, an AoE (roughly the same size as a tower) centered on the player goes off and will kill any other player hit.</li>
      <li>While the debuff is active, it can be passed to other players by touching them.</li>
      <li>When passed, the player gains a Performance Debugger buff.</li>
    </ul>
    <p><b>Performance Debugger</b></p>
    <ul><li>Prevents the player from receiving a Critical Performance Bug.</li></ul></td>
  </tr>
</table>

</details>
</div>

### First iteration

<table>
  <tr>
    <td width="50%"><p><b>1.</b> Omega casts Hello, World, and players get their debuffs.</p><ul><li><b>Check which coloured-debuffs go with Critical Overflow and/or Critical Synchronization.</b></li></ul><p><em>In this example:</em></p>
    <ul>
      <li><em>Critical Overflows start with Critical Performance (blue Nisis), so will go to blue towers.
        <ul><li>Local Regressions follow Critical Overflows to the same colour (blue).</li></ul>
      </em></li>
      <li><em>Critical Synchronization start with Critical Underflow (red Nisis), so will go with red towers.
        <ul><li>Remote Regressions follow Critical Synchronizations to the same colour (red).</li></ul></em></li>
    </ul>
    </td>
    <td><img src="../images/03_omega_reconfigured/hello_world_1_1.jpg"></td>
  </tr>
  <tr>
    <td><p><b>2.</b> Pair up and move to your towers.</p><ul><li>Critical Overflow and red/green tethered players pair up and move to their towers <em>(blue in this example).</em></li><li>Critical Synchronization and blue tethered players pair up and move to their towers <em>(red in this example)</em></li></ul><p>Note the red/green tethered players are on the outside of their coloured towers, while the blue tethered players are between their coloured towers.</p></td>
    <td><img src="../images/03_omega_reconfigured/hello_world_1_2.jpg"></td>
  </tr>
  <tr>
    <td><p><b>3.</b> The first set of tethers manifest.</p><p>Towers, Critical Overflow Bugs, and Critical Synchronization Bugs resolve.</p><ul><li>Critical Overflow Bugs transfer to the red/green tethered players.</li><li>Critical Synchronisations transfer to the blue tethered players.</li></ul></td>
    <td><img src="../images/03_omega_reconfigured/hello_world_1_3.jpg"></td>
  </tr>
  <tr>
    <td><p><b>4.</b> Pass Critical Underflow and Critical Performance Bugs.</p><p>Blue-tethered players also break their tether in the process.</p></td>
    <td><img src="../images/03_omega_reconfigured/hello_world_1_4.jpg"></td>
  </tr>
  <tr>
    <td><p><b>5.</b> Red/green tethered players move together to break their tether.</p><p>Avoid the explosions from Critical Underflow and Critical Performance.</p></td>
    <td><img src="../images/03_omega_reconfigured/hello_world_1_5.jpg"></td>
  </tr>
</table>

### Second iteration

All players rotate their roles for the second iteration.

<table>
  <tr>
    <td width="50%"><p><b>6.</b> Pair up and move to your towers.</p><ul><li>Critical Overflow and red/green tethered players pair up and move to their towers.</li><li>Critical Synchronization and blue tethered players pair up and move to their towers.</li></ul></td>
    <td><img src="../images/03_omega_reconfigured/hello_world_2_1.jpg"></td>
  </tr>
  <tr>
    <td><p><b>7.</b> The next set of tethers manifest.</p><p>Towers, Critical Overflow Bugs, and Critical Synchronization Bugs resolve.</p></td>
    <td><img src="../images/03_omega_reconfigured/hello_world_2_2.jpg"></td>
  </tr>
  <tr>
    <td><p><b>8.</b> Pass Critical Underflow and Critical Performance Bugs.</p><p>Blue-tethered players also break their tether in the process.</p></td>
    <td><img src="../images/03_omega_reconfigured/hello_world_2_3.jpg"></td>
  </tr>
  <tr>
    <td><p><b>9.</b> Red/green tethered players move together to break their tether.</p><p>Avoid the explosions from Critical Underflow and Critical Performance.</p></td>
    <td><img src="../images/03_omega_reconfigured/hello_world_2_4.jpg"></td>
  </tr>
</table>

### Third iteration

All players rotate their roles again for the third iteration.

<table>
  <tr>
    <td width="50%"><p><b>10.</b> Pair up and move to your towers.</p><ul><li>Critical Overflow and red/green tethered players pair up and move to their towers.</li><li>Critical Synchronization and blue tethered players pair up and move to their towers.</li></ul></td>
    <td><img src="../images/03_omega_reconfigured/hello_world_3_1.jpg"></td>
  </tr>
  <tr>
    <td><p><b>11.</b> The third set of tethers manifest.</p><p>Latent Defect, Towers, Critical Overflow Bugs, and Critical Synchronization Bugs resolve.</p></td>
    <td><img src="../images/03_omega_reconfigured/hello_world_3_2.jpg"></td>
  </tr>
  <tr>
    <td><p><b>12.</b> Pass Critical Underflow and Critical Performance Bugs.</p><p>Blue-tethered players also break their tether in the process.</p></td>
    <td><img src="../images/03_omega_reconfigured/hello_world_3_3.jpg"></td>
  </tr>
  <tr>
    <td><p><b>13.</b> Red/green tethered players move together to break their tether.</p><p>Avoid the explosions from Critical Underflow and Critical Performance.</p></td>
    <td><img src="../images/03_omega_reconfigured/hello_world_3_4.jpg"></td>
  </tr>
</table>

## Fourth iteration

All players rotate their roles again for the fourth (and final) iteration.

This time around, there are two differences:

1. Red/green tethers will **join** the blue tethers at Critical Synchronizations instead of getting hit by Critical Overflow and break **first**.
2. Players will **not** pass Critical Underflow and Critical Performance.

<table>
  <tr>
    <td width="50%"><p><b>14.</b> Pair up and move to your towers.</p><ul><li><b>Red/green tethered players will be with Critical Synchronization this time.</b></li><li>Critical Synchronization, blue tethered players, and red/green tethered players group up and move to their towers.</li></ul></td>
    <td><img src="../images/03_omega_reconfigured/hello_world_4_1.jpg"></td>
  </tr>
  <tr>
    <td><p><b>15.</b> The last set of tethers manifest.</p><p>Latent Defect, Towers, Critical Overflow Bugs, and Critical Synchronization Bugs resolve.</p><p>This should immediately break the red/green tethers- break them if they have not.</p></td>
    <td><img src="../images/03_omega_reconfigured/hello_world_4_2.jpg"></td>
  </tr>
  <tr>
    <td><p><b>16.</b> <b>Do not</b> pass Critical Underflow and Critical Performance Bugs.</p><p>Blue-tethered players break their tether.</p></td>
    <td><img src="../images/03_omega_reconfigured/hello_world_4_3.jpg"></td>
  </tr>
  <tr>
    <td><p><b>17.</b> Avoid the explosions from Critical Underflow and Critical Performance.</p></td>
    <td><img src="../images/03_omega_reconfigured/hello_world_4_4.jpg"></td>
  </tr>
  <tr>
    <td><p><b>18.</b> All players have resolved their debuffs, and there are no more bugs remaining.</p><p>Importantly, all players still have the Overflow Debugger buffs so Omega's Critical Error will not apply another round of Critical Overflows on the party.</p></td>
    <td><img src="../images/03_omega_reconfigured/hello_world_4_5.jpg"></td>
  </tr>
</table>

## Oversampled Wave Cannon

<div style="background-color: #200 ; padding: 10px; border: 1px solid;">
<b>UNDER CONSTRUCTION!</b>
</div>

I currently favour the following setup, although may reconsider this in the future.

<table>
  <tr>
    <td><img src="../images/03_omega_reconfigured/monitors_pt_left.jpg"></td>
    <td><img src="../images/03_omega_reconfigured/monitors_pt_right.jpg"></td>
  </tr>
</table>

## Frequently Asked Questions

<details markdown=block>
<summary><b>[Local Regression]</b> Why do the Local Regression players not stand with the Critical Overflows in the final iteration?</summary>
<table>
  <tr><td><p>Omega casts "Critical Error" at the end of Hello, World.</p><p>This will apply a new Critical Overflow Bug onto <em>all</em> players. However, because all players have the Critical Overflow Debugger buff, this additional Critical Overflow Bug is blocked.</p><p>If the Local Regression players stayed with the Critical Overflow players in the final iteration, their Critical Overflow Debugger buffs would get consumed there instead.</p><p>As as result, they won't have the Critical Overflow Debugger buff when Omega casts Critical Error, and will get another round of Critical Overflows that will last into Oversampled Wave Cannon.</p></td></tr>
</table>
</details>