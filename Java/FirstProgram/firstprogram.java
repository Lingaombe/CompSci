import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class firstprogram extends HttpServlet {

    public void doGet(HttpServletRequest hsr,
                      HttpServletResponse hsrs)
                      throws ServletException, IOException {

        hsrs.setContentType("text/html");
        PrintWriter out = hsrs .getWriter();
        out.println("<h2>Hello Servlet!!</h2>");
    }
}

