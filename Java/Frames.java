import java.awt.event.*;
import javax.swing.*;
import java.util.*;
import java.awt.event.ActionListener;
import java.awt.FlowLayout;

class Frames implements ActionListener{
	JFrame f;
	JButton b1,b2;
	JTextField t;
	
	
	Frames(){
		f = new JFrame("Hannah");
		f.setLayout(new FlowLayout());
		f.setSize(300,300);
		b1 = new JButton("iwe");
		b2 = new JButton("ine");
		t = new JTextField(20);
		b1.addActionListener(this);
		b2.addActionListener(this);
		f.add(b1);
		f.add(b2);
		f.add(t);
		f.pack();
		f.setVisible(true);
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	
	public void actionPerformed(ActionEvent ae){
		if(ae.getSource() == b1){
			t.setText("iwensotu nawe");
		}
		else if(ae.getSource() == b2){
			t.setText("ine ndataninso?");
		}
	}
	
	public static void main(String[] a){
		Frames fs = new Frames();
	} 
}
