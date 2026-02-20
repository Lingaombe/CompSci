import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class loginform extends HttpServlet{
	public void doGet(HttpServletRequest hsr, HttpServletResponse hsrs) throws ServletException, IOException{
		hsrs.setContentType("text/html");
	
		String unm = hsr.getParameter("uname");
		PrintWriter out = hsrs.getWriter();
		out.println("<html><body>");
		out.println("<h2>Hello "  +unm);
		out.println("</body></html>");
	
	
	}
}
