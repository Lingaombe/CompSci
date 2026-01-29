import javax.swing.*;
import java.awt.event.*;
//import java.awt.flowchart;
import java.awt.event.ActionListener;
import java.sql.*;
import java.sql.Connection;
import java.sql.DriverManager;

class login implements ActionListener{
	JFrame f,f1;
	JLabel l1,l2,l3,l4,l5,l6,l7,l8;
	JButton b,b1,b2;
	JTextField t1,t2,t3,t4,t5,t7;
	JPasswordField t6,t8;
	
	login(){
		f = new JFrame("sign up");
		f1 = new JFrame("login");
		l1 = new JLabel("enter name");
		l1.setBounds(20,20,100,30);
		l2 = new JLabel("enter email");
		l2.setBounds(20,60,100,30);
		l3 = new JLabel("enter mobile no");
		l3.setBounds(20,100,100,30);
		l4 = new JLabel("enter DOB");
		l4.setBounds(20,140,100,30);
		l5 = new JLabel("enter user ID");
		l5.setBounds(20,180,100,30);
		l6 = new JLabel("enter password");
		l6.setBounds(20,220,100,30);
		l7 = new JLabel("enter name");
		l7.setBounds(20,20,100,30);
		l8 = new JLabel("enter password");
		l8.setBounds(20,60,100,30);
		t1 = new JTextField(12);
		t1.setBounds(120,20,100,30);
		t2 = new JTextField(20);
		t2.setBounds(120,60,100,30);
		t3 = new JTextField(20);
		t3.setBounds(120,100,100,30);
		t4 = new JTextField(20);
    t4.setBounds(120,140,100,30);
		t5 = new JTextField(20);
		t5.setBounds(120,180,100,30);
		t6 = new JPasswordField(20);
		t6.setBounds(120,220,100,30);
		t7 = new JTextField(12);
		t7.setBounds(120,20,100,30);
		t8 = new JPasswordField(20);
		t8.setBounds(120,60,100,30);
		b = new JButton("sign up");
		b.setBounds(40,260,100,30);
		b2 = new JButton("go to login");
		b2.setBounds(200,260,200,30);
		b1 = new JButton("login");
		b1.setBounds(40,100,100,30);
		
		f.setLayout(null);
		f.setSize(300,300);
		f1.setLayout(null);
		f1.setSize(300,300);
		f.add(l1);
		f.add(t1);
		f.add(l2);
		f.add(t2);
		f.add(l3);
		f.add(t3);
		f.add(l4);
		f.add(t4);
		f.add(l5);
		f.add(t5);
		f.add(l6);
		f.add(t6);
		f.add(b);
		f.add(b2);
		f.pack();
		
		f1.add(l7);
		f1.add(t7);
		f1.add(l8);
		f1.add(t8);
		f1.add(b1);
		f1.pack();
		b1.addActionListener(this);
		b2.addActionListener(this);
		b.addActionListener(this);
		
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		f.setExtendedState(JFrame.MAXIMIZED_BOTH);
		f.setVisible(true);
		f1.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		f1.setExtendedState(JFrame.MAXIMIZED_BOTH);
		f1.setVisible(false);
	}
	
	public void actionPerformed(ActionEvent ae){
		if(ae.getSource() == b){
			try{
				String name = t1.getText();
				String email = t2.getText();
				String mobile = t3.getText();
				String DOB = t4.getText();
				String userID = t5.getText();
				String password = t6.getText();
				System.out.println("apa tidafika1");
				
				String url = "jdbc:mysql://localhost:3306/first";
				String user = "user";
				String psw = "mysql";
				System.out.println("apa tidafika2");
				Class.forName("com.mysql.cj.jdbc.Driver");
				Connection conn = DriverManager.getConnection(url, user, psw);
				System.out.println("apa tidafika3");
				
				String q = "INSERT INTO users (name, email, mobile, DOB, userID, password) VALUES (?,?,?,?,?,?)";
				PreparedStatement ps = conn.prepareStatement(q);
				System.out.println("apa tidafika4");
				ps.setString(1, name);
				ps.setString(2, email);
				ps.setString(3, mobile);
				ps.setString(4, DOB);
				ps.setString(5, userID);
				ps.setString(6, password);
				System.out.println("apa tidafika5");
				int rowsAffected = ps.executeUpdate();
				if (rowsAffected>0){
				  JOptionPane.showMessageDialog(f, "Record Inserted");
				}
				f1.setVisible(true);
				ps.close();
				conn.close();
			}
			catch(Exception e){
				JOptionPane.showMessageDialog(f,"Record Not Inserted");
			}
			}
			if(ae.getSource() == b2){
			  try{
				  f1.setVisible(true);
			  }
			  catch(Exception e){
				  JOptionPane.showMessageDialog(f,"Record Not Inserted");
			  }
			}
			if(ae.getSource() == b1){
			  try{
				  String name = t7.getText();
				  String password = t8.getText();
				  System.out.println(name);
				  System.out.println(password);
				  System.out.println("apa tidafika6");
				  
				  String url = "jdbc:mysql://localhost:3306/first";
				  String user = "user";
				  String psw = "mysql";
				  System.out.println("apa tidafika7");
				  Class.forName("com.mysql.cj.jdbc.Driver");
				  Connection conn = DriverManager.getConnection(url, user, psw);
				  System.out.println("apa tidafika8");
				  
				  String query = "SELECT COUNT(*) AS rowcount FROM users WHERE name = ? and password = ?";
				  
				  System.out.println("apa tidafika9");
				  
				  PreparedStatement st = conn.prepareStatement(query);
				  st.setString(1, name);
				  st.setString(2, password);
          ResultSet rs = st.executeQuery();
          int c = 0;
          
				  if (rs.next()){
				    c = rs.getInt("rowcount");
				    System.out.println(c);
				    System.out.println("apa tidafika10");
				  }
				  else{
				    System.out.println("apa tidafika12");
				  }
				  if(c==1){
				    JOptionPane.showMessageDialog(f, "Logged In");
				    System.out.println("apa tidafika11");
				  }
				conn.close();
			}
			catch(Exception e){
				JOptionPane.showMessageDialog(f,"Not Logged In");
			}
		}
	}
	
	public static void main(String[] args){
		login l = new login();
	}
}
