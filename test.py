import pandas as pd

# 讀取剛剛下載並解壓縮好的 CSV 檔案
# 請確保檔名和你資料夾裡的一模一樣
df = pd.read_csv('Grocery_Inventory_and_Sales_Dataset.csv')

# 可以在終端機印出前 5 筆資料，確認有沒有讀取成功
print("=== 原始資料預覽 ===")
print(df.head())
print("\n")


# ---------------------------------------------------------
# 作業要求 (1)：計算每個商品的總庫存價值
# 邏輯：總庫存價值 = 庫存數量 (Stock_Quantity) * 單價 (Unit_Price)
# ---------------------------------------------------------
# 1. 將 Unit_Price 轉成字串，拔掉 '$' 和 ',' 符號，最後轉換成浮點數 (float)
df['Unit_Price'] = df['Unit_Price'].astype(str).str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)

# 2. 為了保險起見，確保 Stock_Quantity 也是數字格式
df['Stock_Quantity'] = df['Stock_Quantity'].astype(float)

# 3. 再執行你原本的乘法公式，就不會報錯囉！
df['Total_Inventory_Value'] = df['Stock_Quantity'] * df['Unit_Price']
df['Total_Inventory_Value'] = df['Stock_Quantity'] * df['Unit_Price']

print("=== (1) 前五筆商品的總庫存價值 ===")
print(df[['Product_Name', 'Total_Inventory_Value']].head())
print("\n")


# ---------------------------------------------------------
# 作業要求 (2)：找出最暢銷
# 邏輯：找出銷售量 (Sales_Volume) 最高的那一列
# ---------------------------------------------------------
# idxmax() 可以幫我們找出數值最大那筆資料的索引值 (index)
best_selling_idx = df['Sales_Volume'].idxmax()

# 透過 loc 把那一整筆資料抓出來
best_selling_product = df.loc[best_selling_idx]

print("=== (2) 最暢銷商品資訊 ===")
print(f"商品名稱: {best_selling_product['Product_Name']}")
print(f"銷售量: {best_selling_product['Sales_Volume']}")
print("\n")


# ---------------------------------------------------------
# 作業要求 (3)：計算 9 折後的收入
# 邏輯：銷售量 (Sales_Volume) * 單價 (Unit_Price) * 0.9
# ---------------------------------------------------------
df['Revenue_After_Discount'] = df['Sales_Volume'] * df['Unit_Price'] * 0.9

print("=== (3) 前五筆商品打 9 折後的收入 ===")
print(df[['Product_Name', 'Revenue_After_Discount']].head())
print("\n")


# ---------------------------------------------------------
# 最終步驟：將算好的結果存成新的檔案 (可選)
# 這樣之後推送到 GitHub 上，老師也能看到你處理完的完整資料表
# ---------------------------------------------------------
df.to_csv('Grocery_Analysis_Result.csv', index=False)
print("✅ 運算結束！結果已經存成 'Grocery_Analysis_Result.csv'")