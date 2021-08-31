
import mysql.connector
import pandas as ps

"""
Data Access class - Mongo DB connector
5 Classification rules
"""


class StoreClassifiers:

    """
    Defining 5 GET definitions for API server
    """

    def __init__(self):
        """
        Pymongo connector
        """

    def get_loyal_member(self,customers_df):
        """
        To Fetch Customer with Max Visits
        :return: List of top 3 CMVs
        """

        max_visits_customer = customers_df[customers_df["visits"]==customers_df["visits"].max()]["name"]
        print("\n Loyal member is : ", max_visits_customer)
        loyal_member = str(max_visits_customer.item()) + " is our loyal member"
        return loyal_member

    def get_senior_customer(self,customers_df):
        """
        To Fetch senior customers for eligible discount of 10%
        :return: List of top 3 SCs
        """
        print("\n SVC DF:",customers_df)
        max_age = customers_df.age.max()
        senior_customer = customers_df[customers_df["age"]==customers_df["age"].max()]["name"]
        print("\n Senior Customer is : ",senior_customer)
        return str(senior_customer.item())

    def get_top_revenue_customer(self,orders_df,customers_df):
        """
        To Fetch TRC
        :return: List of top 3 TRCs
        """
        trc_id = orders_df[orders_df["total"]==orders_df["total"].max()]["customer_id"]
        tr_customer = customers_df[customers_df["customer_id"] == trc_id.item()]["name"]
        trc_name = str(tr_customer.item()) + " is our top revenue customer"
        return trc_name

    @classmethod
    def get_total_revenue(self,orders_df):
        """
        To Fetch TR
        :return: TR
        """
        total_revenue = orders_df["total"].sum()
        
        return "Total revenue is : "+str(total_revenue)

    @classmethod
    def generate_df_from_mysql(self):


        # connecting to the petstore_db
        petstore_db_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="dbpass1",
            database="petstore_schema")

        # preparing a cursor object
        ps_cursor = petstore_db_conn.cursor()

        # selecting query
        customers_query = "SELECT * FROM petstore_schema.customers"
        ps_cursor.execute(customers_query)
        cust_result = ps_cursor.fetchall()
        customers_df = ps.read_sql(customers_query, petstore_db_conn)

        orders_query = "SELECT * FROM petstore_schema.orders"
        ps_cursor.execute(orders_query)
        orders_result = ps_cursor.fetchall()
        orders_df = ps.read_sql(orders_query, petstore_db_conn)


        print("\n CUSTOMERS DF is: \n",customers_df.head())
        print("\n\n ORDERS DF is: \n", orders_df.head())
        # disconnecting from server
        petstore_db_conn.close()

        return orders_df,customers_df