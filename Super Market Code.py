# %%
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("SUPER MARKET DATA.xlsx")
print(df)
print(df.dtypes)
df.dropna(inplace=True)

# %%
df['Date']= pd.to_datetime(df['Date'])
df['MONTH'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('MONTH')['Sales'].sum().reset_index()
highest_sales_month = monthly_sales.loc[monthly_sales['Sales'].idxmax()]
lowest_sales_month = monthly_sales.loc[monthly_sales['Sales'].idxmin()]
print(f"Highest sales month: {highest_sales_month['MONTH']} with sales of {highest_sales_month['Sales']}")
print(f"Lowest sales month: {lowest_sales_month['MONTH']} with sales of {lowest_sales_month['Sales']}")

plt.figure(figsize=(12,6))
plots=plt.plot(monthly_sales['MONTH'].astype(str), monthly_sales['Sales'], marker='o', color='blue', label='Sales Trend')
plt.title('Monthly Sales Trend')
plt.xlabel('Month', fontsize=12, color='Red')
plt.ylabel('Sales', fontsize=12, color='Red')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
Sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()
sales_by_category_sorted = Sales_by_category.sort_values(by='Sales', ascending=False)   
highest_sales_category = sales_by_category_sorted.iloc[0]
lowest_sales_category = sales_by_category_sorted.iloc[-1]
print(f"Highest sales category: {highest_sales_category['Category']} with sales of {highest_sales_category['Sales']}")
print(f"Lowest sales category: {lowest_sales_category['Category']} with sales of {lowest_sales_category['Sales']}")
plt.figure(figsize=(12,6))
bars=plt.bar(sales_by_category_sorted['Category'], sales_by_category_sorted['Sales'], color='green', label='Sales by Category')
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2.0,  
        height,                                
        f'{height:,.0f}',                     
        ha='center', va='bottom',              
        fontsize=10, fontweight='bold', color='black')
bars[0].set_color('red') ,bars[-1].set_color('blue')
plt.title('Sales by Category')
plt.xlabel('Category', fontsize=12, color='Red')
plt.ylabel('Sales', fontsize=12, color='Red')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
gender_sales = df.groupby('Gender')['Sales'].sum().reset_index()
highest_sales_gender = gender_sales.loc[gender_sales['Sales'].idxmax()]
lowest_sales_gender = gender_sales.loc[gender_sales['Sales'].idxmin()]
print(f"Highest sales gender: {highest_sales_gender['Gender']} with sales of {highest_sales_gender['Sales']}")
print(f"Lowest sales gender: {lowest_sales_gender['Gender']} with sales of {lowest_sales_gender['Sales']}")
plt.figure(figsize=(8,6))
plt.pie(gender_sales['Sales'], labels=gender_sales['Gender'], autopct='%1.1f%%',  colors=['#ff9999','#66b3ff'])
plt.title('Sales Distribution by Gender')
plt.axis('equal')
plt.tight_layout()
plt.show()

# %%
Payment1=df['Payment'].value_counts().reset_index()
Payment1.columns=['Payment','Count']
total_Payment1 =Payment1['Count'].sum()
Payment1['percentage']=Payment1['Count']/total_Payment1*100
highest_method=Payment1.iloc[Payment1['Count'].idxmax()]
lowest_method=Payment1.loc[Payment1['Count'].idxmin()]

print(f"Highest Payment method: {highest_method['percentage']} with method of {highest_method['Payment']}")
print(f"Lowest Payment method: {lowest_method['percentage']} with method of {lowest_method['Payment']}")
plt.Figure(figsize=(10,10))
plt.pie(Payment1['Count'],autopct='%1.1f%%',labels=Payment1['Payment'])
plt.title('payment_metod')



# %%
df['Date']= pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
product_sale_mothly=df.groupby(['Month','Product'])['Sales'].sum().reset_index()
product_sale_mothly=product_sale_mothly.sort_values(by='Sales',ascending=False)
print(f"Highest product salse of {product_sale_mothly.iloc[0]['Month']} with the sales of {product_sale_mothly['Sales']} and product is {product_sale_mothly['Product']}")
print(f"Lowest product salse of {product_sale_mothly.iloc[-1]['Month']} with the sales of {product_sale_mothly['Sales']} and product is {product_sale_mothly['Product']}")
plt.Figure(figsize=(6,17))
plt.bar(product_sale_mothly['Product'],product_sale_mothly['Sales'])

plt.title('Monthly sales by catagory',color='red',fontsize=15)
plt.xlabel('Product',color='red',fontsize=12)
plt.ylabel('Sales',color='red',fontsize=12)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show

# %%

region_sales=df['City'].value_counts().reset_index()

region_sales=df.groupby('City')['Sales'].sum().reset_index()

region_sales.sort_values(by='Sales',ascending=False)
print(region_sales)
plt.Figure(figsize=(6,9))
bars=plt.bar(region_sales['City'],region_sales['Sales'])
bars[0].set_color('red'),bars[-1].set_color('green')
for bar in bars:
    height = bar.get_height()
    plt.text( bar.get_x() + bar.get_width() / 2.0,  
            height,                                
            f'{height:,.0f}',                     
            ha='center', va='bottom',              
            fontsize=10, fontweight='bold', color='black')

plt.title('city wise sales',color='red')
plt.xlabel('City',color='red')
plt.ylabel('Sales',color='red')

plt.xticks(rotation=45)
plt.show()

# %%
Customer_type=df['Customer Type'].value_counts().reset_index()
Customer_type.columns=['Customer type','Count']
total_Customer =Customer_type['Count'].sum()

highest_type=Customer_type.iloc[Customer_type['Count'].idxmax()]
lowest_type=Customer_type.loc[Customer_type['Count'].idxmin()]
print(f"Lowest Payment type: {lowest_type['Count']} with method of {lowest_type['Customer type']}")
print(f"highest Payment type: {highest_type['Count']} with method of {highest_type['Customer type']}")
print(Customer_type)
plt.Figure(figsize=(1,1))
plt.pie(Customer_type['Count'],labels=Customer_type['Customer type'],autopct='%1.1f%%',colors=['red','green'])
plt.title('Customer type')
plt.axis('equal')
plt.tight_layout
plt.show

# %%
jaipur_sales=(df[df['City']=='Jaipur'].groupby('Product')['Sales'].sum().reset_index().sort_values(by='Sales',ascending=False))
highest_sale_of_jaipur= jaipur_sales.loc[jaipur_sales['Sales'].idxmax()]
lowest_sales_of_jaipur=jaipur_sales.loc[jaipur_sales['Sales'].idxmin()]
#print(jaipur_sales)
#print(highest_sale_of_jaipur
#      ,lowest_sales_of_jaipur)
print(f"highest sales product of jaipur:{highest_sale_of_jaipur['Product']} with the sales of: {highest_sale_of_jaipur['Sales']}")
print(f"Lowest sales product of jaipur:{lowest_sales_of_jaipur['Product']} with the sales of: {lowest_sales_of_jaipur['Sales']}")
plt.Figure(figsize=(5,8))
bars=plt.bar(jaipur_sales['Product'],jaipur_sales['Sales'])
bars[0].set_color('lightgreen'),bars[-1].set_color('red')
plt.xticks(rotation=90)
plt.xlabel('Sales',color='red',fontweight='bold',fontsize=14)
plt.ylabel('product',color='red',fontweight='bold',fontsize=14)
plt.title('jaipur_sales',color='red',fontweight='bold',fontsize=18)
plt.show()

# %%
Mumbai_sales=(df[df['City']=='Mumbai'].groupby('Product')['Sales'].sum().reset_index().sort_values(by='Sales',ascending=False))
highest_sale_of_Mumbai= Mumbai_sales.loc[Mumbai_sales['Sales'].idxmax()]
lowest_sales_of_Mumbai=Mumbai_sales.loc[Mumbai_sales['Sales'].idxmin()]
#print(jaipur_sales)
#print(highest_sale_of_jaipur
#      ,lowest_sales_of_jaipur)
print(f"highest sales product of Mumbai:{highest_sale_of_Mumbai['Product']} with the sales of: {highest_sale_of_Mumbai['Sales']}")
print(f"Lowest sales product of Mumbai:{lowest_sales_of_Mumbai['Product']} with the sales of: {lowest_sales_of_Mumbai['Sales']}")
plt.Figure(figsize=(5,8))
bars=plt.bar(Mumbai_sales['Product'],Mumbai_sales['Sales'])
bars[0].set_color('lightgreen'),bars[-1].set_color('red')
plt.xticks(rotation=90)
plt.xlabel('Sales',color='red',fontweight='bold',fontsize=14)
plt.ylabel('product',color='red',fontweight='bold',fontsize=14)
plt.title('Mumbai_sales',color='red',fontweight='bold',fontsize=18)
plt.show()

# %%
Bengaluru_sales=(df[df['City']=='Bengaluru'].groupby('Product')['Sales'].sum().reset_index().sort_values(by='Sales',ascending=False))
highest_sale_of_Bengaluru= Bengaluru_sales.loc[Bengaluru_sales['Sales'].idxmax()]
lowest_sales_of_Bengaluru=Bengaluru_sales.loc[Bengaluru_sales['Sales'].idxmin()]
#print(jaipur_sales)
#print(highest_sale_of_jaipur
#      ,lowest_sales_of_jaipur)
print(f"highest sales product of Bengaluru:{highest_sale_of_Bengaluru['Product']} with the sales of: {highest_sale_of_Bengaluru['Sales']}")
print(f"Lowest sales product of Bengaluru:{lowest_sales_of_Bengaluru['Product']} with the sales of: {lowest_sales_of_Bengaluru['Sales']}")
plt.Figure(figsize=(5,8))
bars=plt.bar(Bengaluru_sales['Product'],Bengaluru_sales['Sales'])
bars[0].set_color('lightgreen'),bars[-1].set_color('red')
plt.xticks(rotation=90)
plt.xlabel('Sales',color='red',fontweight='bold',fontsize=14)
plt.ylabel('product',color='red',fontweight='bold',fontsize=14)
plt.title('Bengaluru_sales',color='red',fontweight='bold',fontsize=18)
plt.show()

# %%
Delhi_sales=(df[df['City']=='Delhi'].groupby('Product')['Sales'].sum().reset_index().sort_values(by='Sales',ascending=False))
highest_sale_of_Delhi= Delhi_sales.loc[Delhi_sales['Sales'].idxmax()]
lowest_sales_of_Delhi=Delhi_sales.loc[Delhi_sales['Sales'].idxmin()]
#print(jaipur_sales)
#print(highest_sale_of_jaipur
#      ,lowest_sales_of_jaipur)
print(f"highest sales product of Delhi:{highest_sale_of_Delhi['Product']} with the sales of: {highest_sale_of_Delhi['Sales']}")
print(f"Lowest sales product of Delhi:{lowest_sales_of_Delhi['Product']} with the sales of: {lowest_sales_of_Delhi['Sales']}")
plt.Figure(figsize=(5,8))
bars=plt.bar(Delhi_sales['Product'],Delhi_sales['Sales'])
bars[0].set_color('lightgreen'),bars[-1].set_color('red')
plt.xticks(rotation=90)
plt.xlabel('Sales',color='red',fontweight='bold',fontsize=14)
plt.ylabel('product',color='red',fontweight='bold',fontsize=14)
plt.title('Delhi_sales',color='red',fontweight='bold',fontsize=18)
plt.show()

# %%
from io import BytesIO
from docx import Document
from docx.shared import Inches

import matplotlib.pyplot as plt

doc = Document()
doc.add_heading("Supermarket Sales Analysis Report", level=0)

# Add the existing written report.
for line in report_text.splitlines():
    if not line.strip() or set(line.strip()) <= {"=","-"}:
        continue
    if line[:1].isdigit() and ". " in line[:5]:
        doc.add_heading(line, level=1)
    else:
        doc.add_paragraph(line)

def add_chart(title, plot_func):
    fig, ax = plt.subplots(figsize=(10, 5))
    plot_func(ax)
    fig.tight_layout()

    image = BytesIO()
    fig.savefig(image, format="png", dpi=150, bbox_inches="tight")
    image.seek(0)

    doc.add_heading(title, level=2)
    doc.add_picture(image, width=Inches(6.3))
    plt.close(fig)

add_chart("Monthly Sales Trend", lambda ax: (
    ax.plot(monthly_sales["MONTH"].astype(str), monthly_sales["Sales"], marker="o"),
    ax.set(title="Monthly Sales Trend", xlabel="Month", ylabel="Sales"),
    ax.tick_params(axis="x", rotation=45),
    ax.grid(axis="y", alpha=0.3)
))

add_chart("Sales by Category", lambda ax: (
    ax.bar(sales_by_category_sorted["Category"], sales_by_category_sorted["Sales"], color="seagreen"),
    ax.set(title="Sales by Category", xlabel="Category", ylabel="Sales"),
    ax.tick_params(axis="x", rotation=40)
))

add_chart("Sales Distribution by Gender", lambda ax: (
    ax.pie(gender_sales["Sales"], labels=gender_sales["Gender"], autopct="%1.1f%%"),
    ax.set_title("Sales Distribution by Gender")
))

add_chart("Payment Methods", lambda ax: (
    ax.pie(Payment1["Count"], labels=Payment1["Payment"], autopct="%1.1f%%"),
    ax.set_title("Transactions by Payment Method")
))

add_chart("Customer Types", lambda ax: (
    ax.pie(Customer_type["Count"], labels=Customer_type["Customer type"], autopct="%1.1f%%"),
    ax.set_title("Customer Type Distribution")
))

city_sales_sorted = region_sales.sort_values("Sales", ascending=False)
add_chart("Sales by City", lambda ax: (
    ax.bar(city_sales_sorted["City"], city_sales_sorted["Sales"], color="cornflowerblue"),
    ax.set(title="Sales by City", xlabel="City", ylabel="Sales")
))

top_products = (
    df.groupby("Product", as_index=False)["Sales"].sum()
      .sort_values("Sales", ascending=False)
      .head(10)
)
add_chart("Top 10 Products by Sales", lambda ax: (
    ax.bar(top_products["Product"], top_products["Sales"], color="darkorange"),
    ax.set(title="Top 10 Products by Sales", xlabel="Product", ylabel="Sales"),
    ax.tick_params(axis="x", rotation=45)
))

top_month_product = product_sale_mothly.head(10).copy()
top_month_product["Label"] = (
    top_month_product["Product"] + " (" + top_month_product["Month"].astype(str) + ")"
)
add_chart("Top 10 Month–Product Sales", lambda ax: (
    ax.bar(top_month_product["Label"], top_month_product["Sales"], color="mediumpurple"),
    ax.set(title="Top 10 Month–Product Sales", xlabel="Product (Month)", ylabel="Sales"),
    ax.tick_params(axis="x", rotation=55)
))

for city_name, city_df in df.groupby("City"):
    city_products = (
        city_df.groupby("Product", as_index=False)["Sales"].sum()
               .sort_values("Sales", ascending=False)
    )
    add_chart(
        f"Product Sales in {city_name}",
        lambda ax, data=city_products, name=city_name: (
            ax.bar(data["Product"], data["Sales"], color="teal"),
            ax.set(title=f"Product Sales in {name}", xlabel="Product", ylabel="Sales"),
            ax.tick_params(axis="x", rotation=60)
        )
    )

output_file = "supermarket_sales_analysis_with_graphs.docx"
doc.save(output_file)
print(f"Report saved as: {output_file}")


