import streamlit as st
import pandas as pd
import psycopg2

def get_data_from_db():
    db_connection = psycopg2.connect(
        host="192.168.111.12",
        port="5432",
        dbname="RWL",
        user="dilnas_read",
        password="ptc_123456!@"
    )
    
    query = """SELECT *
FROM positions
WHERE vagon_no IN (
    '58632506', '58602285', '58608563', '58632050', '51000073', '58601261', '58601311', 
    '58624149', '58608654', '58623927', '58633579', '58608548', '58632589', '58630062', 
    '58607680', '58623331', '58607599', '58604000', '58624255', '58634890', '58630104', 
    '51009207', '58602301', '58607813', '58633488', '58602335', '58603333', '58604034', 
    '58631698', '58607805', '58607722', '51002442', '58605551', '98695927', '98695935', 
    '98695943', '98695950', '98695968', '98695976', '98695984', '98695992', '98696008', 
    '98696016', '98696024', '98696032', '98696040', '98696057', '98696065', '98696073', 
    '98696081', '98696099', '98696107', '98696115', '99207441', '98696123', '98696131', 
    '98696149', '98696156', '98696164', '98696172', '98696180', '98696206', '98696198', 
    '98478308', '98478316', '98477920', '98477938', '98477946', '98477953', '98478324', 
    '98478340', '98477979', '98477995', '98478019', '98478027', '98478449', '98478050', 
    '98478464', '98478068', '98478076', '98478084', '98478100', '98478118', '98478126', 
    '98478142', '98478159', '98478175', '98478589', '98478183', '98478191', '98478225', 
    '98478233', '98478258', '98478266', '98478274', '98478282', '98478290', '98477904', 
    '98477912', '98477961', '98477987', '98478001', '98478035', '98478043', '98478092', 
    '98478134', '98478167', '98478209', '98478217', '98478241', '98478332', '98478357', 
    '98478365', '98478381', '98478399', '98478407', '98478415', '98478423', '98478431', 
    '98478456', '98478472', '98478480', '98478498', '98478506', '98478514', '98478522', 
    '98478530', '98478548', '98478555', '98478563', '98478571', '98478597', '98478605', 
    '98478613', '98478621', '98478639', '98478647', '98478654', '98478662', '98478670', 
    '98478688', '98478696', '98478704', '98480189', '98480197', '98480205', '98480213', 
    '98480221', '98480239', '98480247', '98480254', '98480262', '98480270', '98480288', 
    '98480296', '98480304', '98480312', '98480320', '98480338', '98480346', '98480353', 
    '98480361', '98480379', '98480387', '98480395', '98480403', '98480411', '98480429', 
    '98480437', '98480445', '98480452', '98480460', '98480478', '98479884', '98479892', 
    '98479900', '98479918', '98479926', '98479934', '98479942', '98479959', '98479967', 
    '98479975', '98479983', '98479991', '98480007', '98480015', '98480023', '98480031', 
    '98480049', '98480056', '98480064', '98480072', '98480080', '98480098', '98480106', 
    '98480114', '98480122', '98480130', '98480148', '98480155', '98480163', '98480171', 
    '98481989', '98481997', '98482003', '98482011', '98482029', '98482037', '98482045', 
    '98482052', '98482060', '98482078', '98482086', '98482094', '98482102', '98482110', 
    '98482128', '98482136', '98482144', '98482151', '98482169', '98482177', '98482185', 
    '98482193', '98482201', '98482219', '98482227', '98482235', '98482243', '98482250', 
    '98482268', '98482276', '98483092', '98483100', '98483118', '98482896', '98482904', 
    '98482912', '98482920', '98482938', '98482946', '98482953', '98483126', '98482961', 
    '98482979', '98482987', '98482995', '98483001', '98483019', '98483027', '98483035', 
    '98483043', '98483050', '98483068', '98483076', '98483084', '98483134', '98483142', 
    '98483159', '98483167', '98483175', '98483183'
);
"""
    
    data = pd.read_sql(query, db_connection)
    
    db_connection.close()
    
    return data

def main():
    st.title("PostgreSQL Data Viewer")

    data = get_data_from_db()
    
    st.write("Here is the data from the database:")
    st.dataframe(data)

    st.sidebar.title("Filter the Data")
    column = st.sidebar.selectbox("Select a column to filter by", data.columns)
    filter_value = st.sidebar.text_input(f"Enter value to filter {column}")

    if filter_value:
        filtered_data = data[data[column].astype(str).str.contains(filter_value, case=False)]
        st.write(f"Filtered Data based on {column} contains '{filter_value}':")
        st.dataframe(filtered_data)
    else:
        st.write("Use the sidebar to filter data.")

if __name__ == "__main__":
    main()
