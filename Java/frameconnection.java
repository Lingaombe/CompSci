import javax.swing.*;
import java.awt.event.*;
//import java.awt.flowchart;
import java.awt.event.ActionListener;
import java.sql.*;
import java.sql.Connection;
import java.sql.DriverManager;

class student implements ActionListener{
	JFrame f;
	JLabel r,n;
	JTextField t1,t2;
	JButton b1,b2;
	student(){
		f=new JFrame("student Details");
		r=new JLabel("Enter roll no");
		r.setBounds(50,50,100,30);
		n=new JLabel("Enter name");
		n.setBounds(50,100,100,30);
		t1=new JTextField(12);
		t1.setBounds(160,50,150,30);
		t2=new JTextField(12);
		t2.setBounds(160,100,150,30);
		b1=new JButton("Save");
		b1.setBounds(160,160,150,30);
		b2=new JButton("Cancel");
		b2.setBounds(360,160,150,30);
		
		f.setLayout(null);
		f.setSize(300,300);
		f.add(r);
		f.add(t1);
		f.add(n);
		f.add(t2);
		
		f.add(b1);
		f.add(b2);
		f.pack();
		
		b1.addActionListener(this);
		b2.addActionListener(this);
		
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		f.setExtendedState(JFrame.MAXIMIZED_BOTH);
		f.setVisible(true);
	}
	
	public void actionPerformed(ActionEvent e){
		if (e.getSource() == b1) {
            try {
                int rno = Integer.parseInt(t1.getText());
                String name = t2.getText();

                String url = "jdbc:mysql://localhost:3306/first";
                String username = "user";
                String password = "mysql";

                Class.forName("com.mysql.cj.jdbc.Driver");
                Connection con = DriverManager.getConnection(url, username, password);

                String sql = "INSERT INTO student (rno, sname) VALUES (?, ?)";
                PreparedStatement ps = con.prepareStatement(sql);

                ps.setInt(1, rno);
                ps.setString(2, name);

                int result = ps.executeUpdate();

                if (result > 0) {
                    JOptionPane.showMessageDialog(f, "Record Inserted Successfully");
                }

                ps.close();
                con.close();

            } catch (Exception ex) {
                JOptionPane.showMessageDialog(f, ex.getMessage());
            }
        }

        if (e.getSource() == b2) {
            t1.setText("");
            t2.setText("");
        }
    }


	
	public static void main(String[] args){
		student s = new student();
    }
}

