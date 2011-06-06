
<%def name="loadSlickGrid(request)"> 
<link rel="stylesheet" 
      href="${a_url}/static/js/SlickGrid/slick.grid.css" 
      type="text/css" 
      media="screen" charset="utf-8" /> 

<script language="javascript" 
        src="${a_url}/static/js/SlickGrid/lib/jquery.event.drag-2.0.min.js">
</script> 

<script language="javascript" 
        src="${a_url}/static/js/SlickGrid/slick.core.js">
</script> 
<script language="javascript" 
        src="${a_url}/static/js/SlickGrid/slick.grid.js">
</script>

<script src="${a_url}/static/js/SlickGrid/slick.dataview.js">
</script>


<script src="${a_url}/static/js/SlickGrid/slick.editors.js">
</script>


</%def>


<%def name="globalScripts(request)"> 
<script type="text/javascript"
        src="${a_url}/static/js/site/globals.js">
</script>
<script type="text/javascript" 
        src="${request.application_url}/static/js/jquery-1.6.1.min.js"></script>
<script type="text/javascript"
        src="${request.application_url}/static/js/jquery-ui-1.8.6.custom.min.js"></script>

</%def>


<%def name="styleSheets(request)">

<link rel="stylesheet" 
      href="${request.application_url}/static/css/boilerplate/screen.css" 
      type="text/css" 
      media="screen" />

<link rel="stylesheet" 
      href="${a_url}/static/css/blitzer/jquery-ui-1.8.12.css" 
      type="text/css" 
      media="screen" />
</%def> 

<%def name="deformStyles(request)">

<link rel="stylesheet" 
      href="${request.application_url}/deform-static/css/form.css" 
      type="text/css" />

<script type="text/javascript"
        src="${request.application_url}/deform-static/scripts/deform.js"></script>

</%def>
