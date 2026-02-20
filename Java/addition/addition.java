import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class addition extends HttpServlet{
	public void doGet(HttpServletRequest hsr, HttpServletResponse hsrs) throws ServletException, IOException{
	hsrs.setContentType("text/html");
	PrintWriter out = hsrs.getWriter();
	
	int n1= Integer.parseInt(hsr.getParameter("num1"));
	int n2= Integer.parseInt(hsr.getParameter("num2"));
	
	out.println("<html><body>");
	out.println("<h2> Addition: "  +(n1+n2));
	out.println("</body></html>");
	
	}
}
