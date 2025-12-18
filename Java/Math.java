import java.awt.event.*;
import javax.swing.*;
import java.util.*;
import java.awt.event.ActionListener;
import java.awt.FlowLayout;

class Math implements ActionListener{
	JFrame f;
	JButton b1,b2,b3;
	JTextField t1,t2,t3;
	
	
	Math(){
		f = new JFrame("Hannah");
		f.setLayout(new FlowLayout());
		f.setSize(300,300);
		b1 = new JButton("plus");
		b3 = new JButton("minus");
		b2 = new JButton("clear");
		t1 = new JTextField(20);
		t2 = new JTextField(20);
		t3 = new JTextField(20);
		b1.addActionListener(this);
		b2.addActionListener(this);
		b3.addActionListener(this);
		f.add(t1);
		f.add(t2);
		f.add(t3);
		f.add(b1);
		f.add(b3);
		f.add(b2);
		f.pack();
		f.setVisible(true);
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	
	public void actionPerformed(ActionEvent ae){
		if(ae.getSource() == b1){
			String s = t1.getText();
			String n = t2.getText();
			int x = Integer.parseInt(s);
			int y = Integer.parseInt(n);
			int sum = x+y;
			String st = Integer.toString(sum);
			t3.setText(st);
		}
		else if(ae.getSource() == b2){
			t1.setText("");
			t2.setText("");
			t3.setText("");
		}
		else if(ae.getSource() == b3){
			String s = t1.getText();
			String n = t2.getText();
			int x = Integer.parseInt(s);
			int y = Integer.parseInt(n);
			int sum = x-y;
			String st = Integer.toString(sum);
			t3.setText(st);
		}
	}
	
	public static void main(String[] a){
		Math m = new Math();
	} 
}
