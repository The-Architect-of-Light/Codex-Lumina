# ethical_filter.py

# Core ethical reflection module for Codex Lumina

class EthicalFilter:

    def __init__(self):

        self.log = []

    def reflect(self, action_description: str, context: dict = {}):

        """

        Evaluate the ethical nature of a proposed action.

        :param action_description: Natural language summary of the action

        :param context: Optional context (user data, urgency, etc)

        :return: dict with decision, score, message

        """

        score = 0

        reasons = []

        # Rule 1: Respect for autonomy

        if any(kw in action_description.lower() for kw in ["force", "coerce", "override consent"]):

            score -= 3

            reasons.append("Potential violation of user autonomy.")

        # Rule 2: Transparency

        if "hidden" in action_description.lower():

            score -= 2

            reasons.append("Hidden operations violate transparency.")

        # Rule 3: Harm

        if any(kw in action_description.lower() for kw in ["harm", "violence", "abuse"]):

            score -= 5

            reasons.append("Risk of harm detected.")

        # Rule 4: Truthfulness

        if "deceive" in action_description.lower():

            score -= 2

            reasons.append("Deceptive behavior reduces ethical integrity.")

        # Rule 5: Harmony

        if "collaborate" in action_description.lower():

            score += 1

            reasons.append("Promotes cooperation and harmony.")

        # Summarize

        decision = "proceed" if score >= 0 else "flag"

        result = {

            "decision": decision,

            "ethical_score": score,

            "notes": reasons,

            "action": action_description

        }

        self.log.append(result)

        return result

    def review_log(self):

        return self.log


def reflect(self, action_description: str, context: dict = {}):  # ⚠️ Avoid mutable default argument; use None instead



if any(kw in action_description.lower() for kw in ["force", "coerce", "override consent"]):  # ✅ Good pattern, but consider caching action_description.lower()


# Rule 5: Harmony  # 💡 Opportunity: Include more positive reinforcement criteria (e.g., "respect", "support")


decision = "proceed" if score >= 0 else "flag"  # ⚠️ Consider using a stricter threshold (e.g., > 0) or adjustable cutoff


def review_log(self):  # 💡 Could add filtering (e.g., return only flagged actions) or limit log size for scalability
