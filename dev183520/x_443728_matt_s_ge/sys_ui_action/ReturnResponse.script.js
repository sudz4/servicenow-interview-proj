
    
function runClientCode(){

    gsftSubmit(null, g_form.getFormElement(), 'return_response');
 }
    
    // Initialize the RESTMessageV2 object with the REST Message and method name
    var r = new sn_ws.RESTMessageV2('x_443728_matt_s_ge.Matt\'s GenAI OpenAI REST Message', 'ChatGPT-POST-L2');

    // Set the parameters for the API call
    r.setStringParameterNoEscape('matts_genai_KEY_0', gs.getProperty('x_443728_matt_s_ge.openai.api.key')); // Use system property for the API key
    r.setStringParameterNoEscape('system_prompt', 'Act as a ServiceNow Certified Master Architect (CMA).');
    r.setStringParameterNoEscape('model', 'gpt-4o-mini');
    r.setStringParameterNoEscape('prompt', 'Who is the CEO of ServiceNow?');

    // Execute the REST message
    var response = r.execute();
    var responseBody = response.getBody();
    var httpStatus = response.getStatusCode();

    // Log the response for debugging purposes
    gs.log('GPT2TESTING     ' + httpStatus);
    gs.log('GPT2TESTING resonse body    ' + responseBody);

    // Check if the response was successful
    if (httpStatus == 200) {
        var parsedResponse = JSON.parse(responseBody);
        gs.log('GPT2TESTING ChatGPT Response =   ' + parsedResponse.choices[0].message.content);
    } else {
        gs.error('GPT2TESTING -> OpenAI API error: ' + httpStatus + ' - ' + responseBody);
    }
    // Log any exceptions that occur during the process
    gs.error('SUDZ #4 -> Exception during API call: ' + ex.message);
