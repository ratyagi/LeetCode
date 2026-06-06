class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tank, start = 0,0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank<0:
                tank = 0
                start = i+1
        return start

# ============================================================================
# LeetCode 134. Gas Station — the `start` variable, explained for future me
# ============================================================================
#
# WHAT `start` IS
#   My current best guess for which station to begin at. Starts at 0. Every
#   time that guess proves impossible, slide it forward. Whatever `start` is
#   left standing when the loop ends is the answer.
#
# THE RESET RULE
#   Walk left to right adding up `tank` (gas[i] - cost[i]):
#     - tank stays >= 0    -> current start still alive, keep going
#     - tank goes negative -> current start is dead. Set start = i+1, tank = 0.
#   Reset tank to 0 (not the negative value) because a fresh start means an
#   empty tank, not the debt just accumulated.
#
# WHY I CAN SKIP STATIONS BETWEEN OLD start AND i  (the greedy part)
#   When the trip dies at i, no station in between works either. Each was
#   reached with surplus; starting there fresh (empty tank) is strictly worse,
#   so it dies even sooner. Throw them all away, jump to i+1, never backtrack.
#   That is what makes this O(n) instead of brute-force O(n^2).
#
# WHY first-positive-diff WAS WRONG
#   It only checks if ONE hop is favorable. The problem needs the cumulative
#   tank to survive the WHOLE circuit. Counterexample:
#       gas  = [5, 1, 2, 3, 4]
#       cost = [4, 4, 1, 5, 1]   ->  diff = [1, -3, 1, -2, 3]
#   First positive diff is index 0, but starting at 0 strands me at station 1.
#   Real answer is index 4 = the start after the LAST reset, not first positive.
#
# WHY i+1 NEVER GOES OUT OF BOUNDS
#   Every reset means the failed segment had a negative sum. A reset on the
#   last station would make every segment negative, so sum(gas) < sum(cost),
#   which already returned -1 up top. So inside the loop the last station never
#   triggers a reset, and start always lands in [0, n-1]. This is why the sum
#   check is load-bearing, not just an early exit.
# ============================================================================
