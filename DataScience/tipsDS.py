import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips)



sns.lineplot(x="size", y="total_bill", marker="o", data=tips)
plt.title("Daily sales trends")
plt.show()

sns.barplot(x="day", y="total_bill", data=tips)
plt.title("Average Bill by Day")
plt.show()

sns.countplot(x="day", data=tips)
plt.title("Number of customers per day")
plt.show()

sns.scatterplot(x="total_bill",y="tip", data=tips)
plt.title("bill vs tips")
plt.show()

sns.boxplot(x="total_bill", y="sex", data=tips)
plt.title("Bill dist by gender")
plt.show()

sns.histplot(x="total_bill", data=tips)
plt.title("Bill dist")
plt.show()

sns.violinplot(x="total_bill", y="day", data=tips)
plt.title("Bill dist by day")
plt.show()

sns.heatmap(tips.corr(numeric_only=True), annot=True)
plt.title("Correlation heatmap")
plt.show()
