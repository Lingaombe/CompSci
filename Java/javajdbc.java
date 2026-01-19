import java.sql.*;
import java.sql.Connection;
import java.sql.DriverManager;

public class javajdbc {
    public static void main(String[] args) throws Exception {
        String url = "jdbc:mysql://localhost:3306/first"; // Database details
        String username = "user"; // MySQL credentials
        String password = "mysql";
        String query = "select * from student"; // Query to be run

        // Load and register the driver
        //Class.forName("com.mysql.cj.jdbc.Driver");
        Class.forName("com.mysql.cj.jdbc.Driver");
        // Establish connection
        Connection con = DriverManager.getConnection(url, username, password);
        System.out.println("Connection Established successfully");

        // Create a statement
        Statement st = con.createStatement();

        // Execute the query
        ResultSet rs = st.executeQuery(query);

        // Process the results
        while (rs.next()) {
            String name = rs.getString("sname"); // Retrieve name from db
            System.out.println(name); // Print result on console
        }

        // Close the statement and connection
        st.close();
        con.close();
        System.out.println("Connection Closed....");
    }
    }
