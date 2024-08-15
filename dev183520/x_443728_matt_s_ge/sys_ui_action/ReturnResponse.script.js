 
 // action_name: Return Response
// onclick: runClientCode(); 

function runClientCode(){

    gsftSubmit(null, g_form.getFormElement(), 'ReturnResponse');
 }

 (function executeAction(current, previous /*null when async*/) {

   // Create the REST message
   var r = new sn_ws.RESTMessageV2('x_443728_matt_s_ge.openai2', 'GetResponse');
   r.setStringParameterNoEscape('system_prompt', 'Act as a ServiceNow Certified Master Architect (CMA).');
   r.setStringParameterNoEscape('model', 'gpt-4o-mini');
   r.setStringParameterNoEscape('prompt', current.ask_here); // Assuming 'ask_question' is a field on the current record

   // Execute the REST call
   var response = r.execute();
   var responseBody = response.getBody();
   var httpStatus = response.getStatusCode();

   // Log the response for debugging
   gs.log("THE RESPONSE BODY IS: " + responseBody);

   // Parse the response
   var responseBodyObj = JSON.parse(responseBody);
   var answer = responseBodyObj.messages.find(msg => msg.role === "assistant").content;

   // Update the form field with the response (assuming you have an 'answer' field on the form)
   current.ask_here = answer; // Replace 'u_answer' with your actual field name for storing the response
   current.update();

   // Insert the data into your custom table
   var openaiGR = new GlideRecord('x_443728_matt_s_ge.openai2'); // Replace with your actual custom table name
   openaiGR.initialize();
   openaiGR.ask_here = current.ask_question;
   openaiGR.answer_here = answer;
   openaiGR.insert();

})(current, previous);
