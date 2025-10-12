import pandas as pd
data = {
"Name":["Ravi","Akash","Rahul","Varun","Tarun"],
"age":[25,None,35,67,33],
"Email":["rav@gmail.com","akash@yahoo.com","rahul@gmail.com","varun@gmail.com","tarun@yahoo.com"],
"Gender":["Male","Female","Male","Male","None"]
}

df=pd.DataFrame(data)
print(df)
print("------------------------------------------------------------------------")
new = df.dropna()
print(new.to_string())
print("------------------------------------------------------------------------")
df.dropna(inplace=True)
print(df)
print("------------------------------------------------------------------------")
df.fillna(30, inplace=True)
print(df)
df.fillna({"age":32},inplace=True)
print(df.to_string())
print("------------------------------------------------------------------------")
x = df["age"].mean()
print(x)
df.fillna({"age":x},inplace=True)
print(df)
print("------------------------------------------------------------------------")
df["Email"] = df["Email"].str.strip()
print(df["Email"])
print("------------------------------------------------------------------------")
df["Email"] = df["Email"].str.replace("gmail", "yahoo", regex=True)
print(df["Email"])
print("------------------------------------------------------------------------")
df["Email"] = df["Email"].where(df["Email"].str.endswith("@gmail.com"))
print(df["Email"])
print("------------------------------------------------------------------------")
df=df.dropna(subset=["Email"])
df=df[df["Email"].str.contains(r'(?i)^[\w.-]+@(gmail|yahoo)\.(com|in)$', na=False)]
print(df)
print("------------------------------------------------------------------------")
