# Part 3: Ethical Reflection

When deploying AI models in real-world environments, potential **biases in datasets** can lead to unfair or discriminatory outcomes. In the case of our predictive model based on the Breast Cancer dataset, one major concern is **data representation**. If the dataset was skewed toward certain demographic groups (e.g., mostly patients from a single ethnic background, region, or gender), the model may generalize poorly to underrepresented populations.

In the context of issue prioritization within software engineering teams, a similar risk arises. If historical bug data overrepresents certain teams or underrepresents others (e.g., due to fewer bug reports or limited access to issue tracking tools), the model might consistently assign low priority to issues from those teams—creating unfair work dynamics.

To mitigate this, fairness tools like **IBM AI Fairness 360** can be integrated. This toolkit provides bias detection metrics (e.g., disparate impact) and bias mitigation algorithms (e.g., reweighting, preprocessing). By using these tools before and after model training, teams can quantify fairness, correct imbalances, and audit performance across groups. This ensures that predictive tools used in software engineering support ethical decision-making and do not perpetuate existing inequalities.
