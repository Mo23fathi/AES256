<!DOCTYPE html>
<!-- saved from url=(0085)https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/blob/main/AES256.py -->
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-a11y-animated-images="system" data-a11y-link-underlines="true" data-js-focus-visible="" data-turbo-loaded=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style type="text/css">.turbo-progress-bar {
  position: fixed;
  display: block;
  top: 0;
  left: 0;
  height: 3px;
  background: #0076ff;
  z-index: 2147483647;
  transition:
    width 300ms ease-out,
    opacity 150ms 150ms ease-in;
  transform: translate3d(0, 0, 0);
}
</style>
    
  
  
  
  
  
  

  

  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/light-0eace2597ca3.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/dark-a167e256da9c.css"><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-d11f2cf8009b.css"><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-ea7373db06c8.css"><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-afa99dcf40f7.css"><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-af6c685139ba.css"><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-578cdbc8a5a9.css"><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-5cb699a7e247.css"><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-9b32204967c6.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/primer-primitives-971c6be3ec9f.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/primer-08e422afeb43.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/global-dbe4faca932a.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/github-36dce55f3db6.css">
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/repository-389a4d55bc31.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/code-aed6ab8a6a15.css">

  


  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["copilot_conversational_ux_history_refs","docset_management_ui","failbot_handle_non_errors","geojson_azure_maps","image_metric_tracking","repository_suggester_elastic_search","turbo_experiment_risky","sample_network_conn_type","no_character_key_shortcuts_in_inputs","custom_inp","remove_child_patch"]}</script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/wp-runtime-17415f19f08e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_dompurify_dist_purify_js-6890e890956f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_stacktrace-parser_dist_stack-trace-parser_esm_js-node_modules_github_bro-a4c183-79f9611c275b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_github_hydro-analytics-client_dist_analytics-client_js-node_modules_gith-6a10dd-e66ebda625fb.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/ui_packages_failbot_failbot_ts-afaa9a250f2e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/environment-2e9dfc62de38.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_github_selector-observer_dist_index_esm_js-9f960d9b217c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_primer_behaviors_dist_esm_focus-zone_js-086f7a27bac0.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_github_relative-time-element_dist_index_js-c76945c5961a.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_fzy_js_index_js-node_modules_github_combobox-nav_dist_index_js-node_modu-344bff-421f7a8c1008.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_details-dialog-elemen-29dc30-a2a71f11a507.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-59c459-d0c49521eb35.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-eb424d-7baa8ec97711.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/github-elements-458e6ff8e072.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/element-registry-cc792c37080f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_github_catalyst_lib_index_js-node_modules_github_hydro-analytics-client_-978abc0-15861e0630b6.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_lit-html_lit-html_js-5b376145beff.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_alive-client_dist-bf5aa2-1b562c29ab8e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_morphdom_dist_morphdom-esm_js-5bff297a06de.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-c91f4ad18b62.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_color-convert_index_js-72c9fbde5ad4.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_scroll-anchoring_dist_scro-231ccf-aa129238d13b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_github_session-resume_dist_index_js-node_modules_primer_behaviors_dist_e-ac74c6-c3eb71941f78.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_primer_behaviors_dist_esm_dimensions_js-node_modules_github_jtml_lib_index_js-95b84ee6bc34.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_github_paste-markdown_dist_index_esm_js-node_modules_github_quote-select-81e6af-77a71286acee.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/app_assets_modules_github_updatable-content_ts-c73b0e1e6f7c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_onfocus_ts-app_ass-421cec-751caa0072bd.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/app_assets_modules_github_sticky-scroll-into-view_ts-cbcee0788fe3.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-467754-b59a2b2827ad.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-b85e9f4f1304.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/behaviors-04737163f502.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-d0256ebff5cd.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/notifications-global-99d196517b1b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_virtualized-list_es_index_js-node_modules_github_template-parts_lib_index_js-878844713bc9.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-c537341-bc0d898369b9.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/app_assets_modules_github_ref-selector_ts-92d4050cac07.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/codespaces-8ea75453efda.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_mini-throt-08ab15-5c0a626f08d8.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_github_mini-th-55cf52-26041abdd865.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/repositories-9449d18bcfd2.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/code-menu-2658b004279a.js.download"></script>
  

  



  
  
  

    
  


  


    


  
  

  
  

    
  
  
  
  



  

  




  

    

  

    
    
      
      
    
    
    
      
      
      

      
      


        


      

        


  <meta http-equiv="x-pjax-version" content="a1b33277d367523daeb7cec318919b1eafa70686f601996cf6fba137a39270ec" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="5dcfbec3488c5fd5a334e287ce6a17058b7d4beb91db2d4d184e4d55bbf1d7d7" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="0a793dcef80159dfdecaf5e38c1e60b55f78b31cd74af6664471eed50a4794b5" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="fdc14cf27ff20de57d816f2ae6cd5c3f43a1ad5f1c4848ef67b6236a3ddd6505" data-turbo-track="reload">

  

      

  

  



    
  


  

  

  
  
  





  

  <style data-styled="active" data-styled-version="5.3.6"></style><style>
    @font-face {
      font-family: 'SegoeUI_online_security'; 
      src: url(chrome-extension://llbcnfanfmjhpedaedhbcnpgeepdnnok/segoe-ui.woff);
    }

    @font-face {
      font-family: 'SegoeUI_bold_online_security'; 
      src: url(chrome-extension://llbcnfanfmjhpedaedhbcnpgeepdnnok/segoe-ui-bold.woff);
    }
</style><style>.av-extension{--dark-blue-background: #183360;--active-blue-font-color: #183360;--modal-header-darkblue-background: #05153f;--grey-font-color: #93a0b5;--background-color: #f1f4f8;--foreground-color: #ffffff;--tertiary-color: #05153f;--primary-font-color: #183360;--green-font-color: #04d289;--red-font-color: #ff3b30;--purple-font-color: #6726ff;--orange-color: #ff8f11;--default-font-size: 18px;--modal-header-background: #f2f2f2;--hover-orange-color: #d97a0e}.av-extension h1{font-family:'Segoe UI Bold';font-size:50px;font-weight:700;line-height:66.5px}.av-extension h2{font-size:30px;padding:0px;margin:5px 0px;margin-top:0px}.av-extension h3{font-size:20px;font-weight:normal;white-space:pre-line}.av-extension p{padding:0px;margin:5px 0px}.av-extension a{text-decoration:none}.av-extension .flex{display:flex}.av-extension .grid{display:grid}.av-extension .fwrap{flex-wrap:wrap}.av-extension .ait{align-items:top}.av-extension .aic{align-items:center}.av-extension .jcl{justify-content:left}.av-extension .jcc{justify-content:center}.av-extension .jcr{justify-content:right}.av-extension .tac{text-align:center}.av-extension .w100{width:100%}.av-extension .sb{font-weight:600}.av-extension .borderButtonColor{color:var(--orange-color);border:3px solid var(--orange-color)}.av-extension .paddinglr{padding:100px 50px}.av-extension .redColor{color:var(--red-font-color);fill:var(--red-font-color)}.av-extension .greenColor{color:var(--green-font-color);fill:var(--green-font-color)}.av-extension .purpleColor{color:var(--purple-font-color)}.av-extension .orangeColor{color:var(--orange-color)}.av-extension .content{color:var(--primary-font-color);margin:auto;max-width:85%;padding-top:30px;padding-bottom:20px}.av-extension .sectionContent{margin-top:80px;margin-bottom:40px;font-size:22px;color:var(--primary-font-color)}.av-extension .btnAction{min-width:170px;padding:10px 25px;color:var(--orange-color);border:2.5px solid var(--orange-color);border-radius:39px;font-weight:600;background-color:transparent}.av-extension .btnAction:hover{background-color:var(--orange-color);color:white}.av-extension .btnDwm{background:linear-gradient(#fff, #fff) padding-box,linear-gradient(to right, #8526ff, #2a26ff) border-box;border:2.5px solid transparent;color:#7644ff}.av-extension .btnDwm:hover{background:linear-gradient(to right, #8526ff, #2a26ff) padding-box,linear-gradient(to right, #8526ff, #2a26ff) border-box;border:2.5px solid transparent}.av-extension .btnBuy{display:flex;align-items:center;justify-content:center;gap:10px;min-width:170px;padding:15px 40px;color:#fff;border-radius:39px;font-weight:600;background-color:var(--tertiary-color);border:none;cursor:pointer}.av-extension .btnBuy:hover{background-color:#0f3cb0}.av-extension .btnBuy:active{background-color:#0f3391}.av-extension .btnBuyOrange{display:flex;align-items:center;justify-content:center;gap:10px;min-width:170px;padding:15px 40px;color:#fff;border-radius:39px;font-weight:600;background-color:var(--orange-color);border:none;cursor:pointer}.av-extension .btnBuyOrange:hover{background-color:#ffa846}.av-extension .btnBuyOrange:active{background-color:#d97a0e}.av-extension .sectionTitle{font-weight:bold;font-size:20px;margin-bottom:25px}.av-extension .sectionTitle img{margin-left:5px;margin-right:13px}.av-extension .fullHeadContent{height:400px;background:var(--tertiary-color);box-shadow:-3px 0px 3px rgba(0,0,0,0.1);border-radius:0px 0px 22px 22px;color:var(--foreground-color)}.av-extension .fullHeadContent img{width:442px}.av-extension .fullHeadContent p{margin:10px}.av-extension .spinner{width:120px;height:120px}@media screen and (min-width: 1500px){.av-extension .content{max-width:70%}}@keyframes spin{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}
</style><style>.checkboxContainer{display:block;position:relative;padding-left:35px;margin-bottom:12px;user-select:none}.checkboxContainer input{position:absolute;opacity:0;height:0;width:0}.checkboxContainer .checkmark{position:absolute;top:0;left:0;height:18px;width:18px;border:1px solid #cad0dd;border-radius:100%}.checkboxContainer .checkmark.greenColor{border:2.5px solid #cad0dd;border-radius:8px}.checkboxContainer:hover input ~ .checkmark{background-color:#cad0dd}.checkboxContainer input:checked ~ .checkmark{background-color:var(--primary-font-color)}.checkboxContainer input:checked ~ .purpleColor{background-color:var(--purple-font-color)}.checkboxContainer input:checked ~ .greenColor{background-color:var(--green-font-color);border:2px solid var(--green-font-color);border-radius:8px}.checkmark:after{content:'';position:absolute;display:none}.checkboxContainer input:checked ~ .checkmark:after{display:block}.checkboxContainer .checkmark:after{left:6px;top:3px;width:3px;height:7px;border:solid white;border-width:0 3px 3px 0;transform:rotate(45deg)}.checkboxContainer .uncheckAll:after{left:7.5px;top:4px;width:0px;height:9px;border-width:0 3px 0 0;transform:rotate(90deg)}.sectionSelectRadio{display:none}.sectionSelectRadio+label{padding:7px 2px;font-size:20px;font-weight:700;margin-right:50px;color:var(--primary-font-color);border:0px;background-color:transparent}.sectionSelectRadio:checked+label{border-bottom:4px solid var(--purple-font-color)}
</style><style id="ms-consent-banner-main-styles">.w8hcgFksdo30C8w-bygqu{color:#000}.ydkKdaztSS0AeHWIeIHsQ a{color:#0067B8}.erL690_8JwUW-R4bJRcfl{background-color:#EBEBEB;border:none;color:#000}.erL690_8JwUW-R4bJRcfl:enabled:hover{color:#000;background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}.erL690_8JwUW-R4bJRcfl:enabled:focus{background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}.erL690_8JwUW-R4bJRcfl:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2);border:none}._1zNQOqxpBFSokeCLGi_hGr{border:none;background-color:#0067B8;color:#fff}._1zNQOqxpBFSokeCLGi_hGr:enabled:hover{color:#fff;background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}._1zNQOqxpBFSokeCLGi_hGr:enabled:focus{background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}._1zNQOqxpBFSokeCLGi_hGr:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,120,215,0.2);border:none}._23tra1HsiiP6cT-Cka-ycB{position:relative;display:flex;z-index:9999;width:100%;background-color:#F2F2F2;justify-content:space-between;text-align:left}div[dir="rtl"]._23tra1HsiiP6cT-Cka-ycB{text-align:right}._1Upc2NjY8AlDn177YoVj0y{margin:0;padding-left:5%;padding-top:8px;padding-bottom:8px}div[dir="rtl"] ._1Upc2NjY8AlDn177YoVj0y{margin:0;padding:8px 5% 8px 0;float:none}._23tra1HsiiP6cT-Cka-ycB svg{fill:none;max-width:none;max-height:none}._1V_hlU-7jdtPiooHMu89BB{display:table-cell;padding:12px;width:24px;height:24px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:24px;line-height:0}.f6QKJD7fhSbnJLarTL-W-{display:table-cell;vertical-align:middle;padding:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:16px}.f6QKJD7fhSbnJLarTL-W- a{text-decoration:underline}._2j0fmugLb1FgYz6KPuB91w{display:inline-block;margin-left:5%;margin-right:5%;min-width:40%;min-width:calc((150px + 3 * 4px) * 2 + 150px);min-width:-webkit-fit-content;min-width:-moz-fit-content;min-width:fit-content;align-self:center;position:relative}._1XuCi2WhiqeWRUVp3pnFG3{margin:4px;padding:5px;min-width:150px;min-height:36px;vertical-align:top;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._1XuCi2WhiqeWRUVp3pnFG3:focus{box-sizing:border-box}._1XuCi2WhiqeWRUVp3pnFG3:disabled{cursor:not-allowed}._2bvsb3ubApyZ0UGoQA9O9T{display:block;position:fixed;z-index:10000;top:0;left:0;width:100%;height:100%;background-color:rgba(255,255,255,0.6);overflow:auto;text-align:left}div[dir="rtl"]._2bvsb3ubApyZ0UGoQA9O9T{text-align:right}div[dir="rtl"] ._2bvsb3ubApyZ0UGoQA9O9T{left:auto;right:0}.AFsJE948muYyzCMktdzuk{position:relative;top:8%;margin-bottom:40px;margin-left:auto;margin-right:auto;box-sizing:border-box;width:640px;background-color:#fff;border:1px solid #0067B8}._3kWyBRbW_dgnMiEyx06Fu4{float:right;z-index:1;margin:2px;padding:12px;border:none;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:13px;display:flex;align-items:center;text-align:center;color:#666;background-color:#fff}div[dir="rtl"] ._3kWyBRbW_dgnMiEyx06Fu4{margin:2px;padding:12px;float:left}.uCYvKvHXrhjNgflv1VqdD{position:static;margin-top:36px;margin-left:36px;margin-right:36px}._17pX1m9O_W--iZbDt3Ta5r{margin-top:0;margin-bottom:12px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:20px;line-height:24px;text-transform:none}._1kBkHQ1V1wu3kl-YcLgUr6{height:446px;overflow:auto}._20_nXDf6uFs9Q6wxRXG-I-{margin-top:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._20_nXDf6uFs9Q6wxRXG-I- a{text-decoration:underline}dl._2a0NH_GDQEQe5Ynfo7suVH{margin-top:36px;margin-bottom:0;padding:0;list-style:none;text-transform:none}dt._3j_LCPv7fyXv3A8FIXVwZ4{margin-top:20px;float:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;list-style:none}.k-vxTGFbdq1aOZB2HHpjh{margin:0;padding:0;border:none}._2Bucyy75c_ogoU1g-liB5R{margin:0;padding:0;border-bottom:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;text-transform:none}._63gwfzV8dclrsl2cfd90r{display:inline-block;margin-top:0;margin-bottom:13px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._1l8wM_4mRYGz3Iu7l3BZR7{display:block}._2UE03QS02aZGkslegN_F-i{display:inline-block;position:relative;left:5px;margin-bottom:13px;margin-right:34px;padding:3px}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{margin:0 0 13px 34px;padding:3px;float:none}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{left:auto;right:5px}._23tra1HsiiP6cT-Cka-ycB *::before,._2bvsb3ubApyZ0UGoQA9O9T *::before,._23tra1HsiiP6cT-Cka-ycB *::after,._2bvsb3ubApyZ0UGoQA9O9T *::after{box-sizing:inherit}._1HSFn0HzGo6w4ADApV8-c4{outline:2px solid rgba(0,0,0,0.8)}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2{display:inline-block;position:relative;margin-top:0;margin-left:0;margin-right:0;height:0;width:0;border-radius:0;cursor:pointer;outline:none;box-sizing:border-box;-webkit-appearance:none;-moz-appearance:none;appearance:none}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{display:block;position:absolute;top:5px;left:3px;height:19px;width:19px;content:"";border-radius:50%;border:1px solid #000;background-color:#fff}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{left:auto;right:3px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:rgba(0,0,0,0.8)}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label{cursor:not-allowed}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label::before{border:1px solid rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2)}._3RJzeL3l9Rl_lAQEm6VwdX{display:block;position:static;float:right;margin-top:0;margin-bottom:0;margin-left:19px;margin-right:0;padding-top:0;padding-bottom:0;padding-left:8px;padding-right:0;width:80%;width:calc(100% - 19px);font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-transform:none;cursor:pointer;box-sizing:border-box}div[dir="rtl"] ._3RJzeL3l9Rl_lAQEm6VwdX{margin:0 19px 0 0;padding:0 8px 0 0;float:left}.nohp3sIG12ZBhzcMnPala{margin-top:20px;margin-bottom:48px}._2uhaEsmeotZ3P-M0AXo2kF{padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._2uhaEsmeotZ3P-M0AXo2kF:focus{box-sizing:border-box}._2uhaEsmeotZ3P-M0AXo2kF:disabled{cursor:not-allowed}._3tOu1FJ59c_xz_PmI1lKV5{float:right;padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._3tOu1FJ59c_xz_PmI1lKV5:focus{box-sizing:border-box}._3tOu1FJ59c_xz_PmI1lKV5:disabled{cursor:not-allowed}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0;padding:0;float:left}@media only screen and (max-width: 768px){._2j0fmugLb1FgYz6KPuB91w,._1Upc2NjY8AlDn177YoVj0y{padding-top:8px;padding-bottom:12px;padding-left:3.75%;padding-right:3.75%;margin:0;width:92.5%}._23tra1HsiiP6cT-Cka-ycB{display:block}._1XuCi2WhiqeWRUVp3pnFG3{margin-bottom:8px;margin-left:0;margin-right:0;width:100%}._2bvsb3ubApyZ0UGoQA9O9T{overflow:hidden}.AFsJE948muYyzCMktdzuk{top:1.8%;width:93.33%;height:96.4%;overflow:hidden}.uCYvKvHXrhjNgflv1VqdD{margin-top:24px;margin-left:24px;margin-right:24px;height:100%}._1kBkHQ1V1wu3kl-YcLgUr6{height:62%;height:calc(100% - 188px);min-height:50%}._2uhaEsmeotZ3P-M0AXo2kF{width:100%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:12px;margin-left:0;width:100%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 12px 0;padding:0;float:none}}@media only screen and (max-width: 768px) and (orientation: landscape), only screen and (max-height: 260px), only screen and (max-width: 340px){.AFsJE948muYyzCMktdzuk{overflow:auto}}@media only screen and (max-height: 260px), only screen and (max-width: 340px){._1XuCi2WhiqeWRUVp3pnFG3{min-width:0}._3kWyBRbW_dgnMiEyx06Fu4{padding:3%}.uCYvKvHXrhjNgflv1VqdD{margin-top:3%;margin-left:3%;margin-right:3%}._17pX1m9O_W--iZbDt3Ta5r{margin-bottom:3%}._1kBkHQ1V1wu3kl-YcLgUr6{height:calc(79% - 64px)}.nohp3sIG12ZBhzcMnPala{margin-top:5%;margin-bottom:10%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:3%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 3% 0;padding:0;float:none}}
</style><style type="text/css" id="ms-consent-banner-theme-styles">._23tra1HsiiP6cT-Cka-ycB {
            background-color: var(--color-scale-gray-9) !important;
        }.w8hcgFksdo30C8w-bygqu {
            color: var(--color-scale-white) !important;
        }.ydkKdaztSS0AeHWIeIHsQ a {
            color: var(--color-scale-purple-2) !important;
        }._2bvsb3ubApyZ0UGoQA9O9T {
            background-color: rgba(23, 23, 23, 0.8) !important;
        }.AFsJE948muYyzCMktdzuk {
            background-color: var(--color-scale-gray-9) !important;
            border: 1px solid var(--color-scale-purple-2) !important;
        }._3kWyBRbW_dgnMiEyx06Fu4 {
            color: var(--color-scale-purple-2) !important;
            background-color: var(--color-scale-gray-9) !important;
        }._1zNQOqxpBFSokeCLGi_hGr {
            border: 1px solid var(--color-scale-white) !important;
            background-color: var(--color-scale-white) !important;
            color: var(--color-scale-black) !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:hover {
            color: var(--color-scale-black) !important;
            background-color: var(--color-scale-purple-2) !important;
            box-shadow: none !important;
            border: 1px solid transparent !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:focus {
            background-color: var(--color-scale-purple-2) !important;
            box-shadow: none !important;
            border: 2px solid var(--color-scale-white) !important;
        }._1zNQOqxpBFSokeCLGi_hGr:disabled {
            opacity: 0.5 !important;
            color: var(--color-scale-black) !important;
            background-color: var(--color-scale-white) !important;
            border: 1px solid transparent !important;
        }.erL690_8JwUW-R4bJRcfl {
            border: 1px solid var(--color-scale-gray-1) !important;
            background-color: var(--color-scale-gray-8) !important;
            color: var(--color-scale-white) !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:hover {
            color: var(--color-scale-white) !important;
            background-color: var(--color-scale-gray-9) !important;
            box-shadow: none !important;
            border: 1px solid var(--color-scale-white) !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:focus {
            background-color: var(--color-scale-gray-9) !important;
            box-shadow: none !important;
            border: 2px solid var(--color-scale-gray-5) !important;
        }.erL690_8JwUW-R4bJRcfl:disabled {
            opacity: 0.5 !important;
            color: var(--color-scale-white) !important;
            background-color: var(--color-scale-gray-7) !important;
            border: 1px solid var(--color-scale-gray-5) !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label::before {
            border: 1px solid var(--color-scale-purple-2) !important;
            background-color: var(--color-scale-gray-9) !important;
        }._1HSFn0HzGo6w4ADApV8-c4 {
            outline: 2px solid var(--color-scale-white) !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked + label::after {
            background-color: var(--color-scale-purple-2) !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::before {
            border: 1px solid var(--color-scale-white) !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::after {
            background-color: var(--color-scale-white) !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::before {
            border: 1px solid var(--color-scale-white) !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::after {
            background-color: var(--color-scale-purple-2) !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled + label::before {
            border: 1px solid rgba(227, 227, 227, 0.2) !important;
            background-color: rgba(227, 227, 227, 0.2) !important;
        }</style><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/react-lib-1fbfc5be2c18.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_primer_octicons-react_dist_index_esm_js-node_modules_primer_react_lib-es-2e8e7c-b299afe58dd7.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_primer_react_lib-esm_Box_Box_js-ebfceb11fb57.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_primer_react_lib-esm_Button_Button_js-0528cb519251.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_primer_react_lib-esm_ActionList_index_js-e001d0eead25.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_primer_react_lib-esm_Overlay_Overlay_js-node_modules_primer_react_lib-es-fa1130-8d276499c3fb.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_primer_react_lib-esm_Text_Text_js-node_modules_primer_react_lib-esm_Text-85a14b-249efa9c2fae.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_primer_behaviors_dist_esm_scroll-into-view_js-node_modules_primer_react_-39745e-56454ece1686.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_primer_react_lib-esm_FormControl_FormControl_js-e905f63cdd0f.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_primer_react_lib-esm_ActionMenu_ActionMenu_js-a3c61ff6363e.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_react-router-dom_dist_index_js-3b41341d50fe.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_primer_react_lib-esm_PageLayout_PageLayout_js-a0f5dc4acaba.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_primer_react_lib-esm_ConfirmationDialog_ConfirmationDialog_js-1396cd0754d9.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_primer_react_lib-esm_Dialog_js-node_modules_primer_react_lib-esm_Label_L-857e1c-55e35df302fc.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_primer_react_lib-esm_TreeView_TreeView_js-5d623f8c8e93.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_primer_react_lib-esm_Flash_Flash_js-node_modules_primer_react_lib-esm_Un-8dc33b-8887e50c8e7f.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_primer_react_lib-esm_Avatar_Avatar_js-node_modules_primer_react_lib-esm_-abca1b-e1f48b432bcb.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_primer_react_lib-esm_AvatarStack_AvatarStack_js-node_modules_primer_reac-d08703-77fc545ff585.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/ui_packages_react-core_create-browser-history_ts-ui_packages_react-core_deferred-registry_ts--ebbb92-64923177f972.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/ui_packages_react-core_register-app_ts-f7fc9821bc0f.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/ui_packages_paths_index_ts-f769a40e764c.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/ui_packages_ref-selector_RefSelector_tsx-858bb94813b1.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/app_assets_modules_github_blob-anchor_ts-app_assets_modules_github_filter-sort_ts-app_assets_-681869-6bbb3d558992.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/ui_packages_commit-attribution_index_ts-ui_packages_commit-checks-status_index_ts-ui_packages-390327-ba6acb060cf4.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/app_assets_modules_react-code-view_pages_CodeView_tsx-154c84961b47.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/react-code-view-95b7b514afad.js.download"></script><link rel="dns-prefetch" href="https://github.githubassets.com/"><link rel="dns-prefetch" href="https://avatars.githubusercontent.com/"><link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com/"><link rel="dns-prefetch" href="https://user-images.githubusercontent.com/"><link rel="preconnect" href="https://github.githubassets.com/" crossorigin=""><link rel="preconnect" href="https://avatars.githubusercontent.com/"><title>encrypt-decrypt-pdf-file-with-AES256-/AES256.py at main · helmii18/encrypt-decrypt-pdf-file-with-AES256-</title><meta name="route-pattern" content="/:user_id/:repository/blob/*name(/*path)" data-turbo-transient=""><meta name="route-controller" content="blob" data-turbo-transient=""><meta name="route-action" content="show" data-turbo-transient=""><meta name="current-catalog-service-hash" content="82c569b93da5c18ed649ebd4c2c79437db4611a6a1373e805a3cb001c64130b7"><meta name="request-id" content="CCA7:325474:2118C05:2167850:65CA5F12" data-turbo-transient="true"><meta name="html-safe-nonce" content="893217b8bf4227bc6b4ffe8b631545abc5509966dc5b09a578b264adc3bf7075" data-turbo-transient="true"><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9oZWxtaWkxOC9lbmNyeXB0LWRlY3J5cHQtcGRmLWZpbGUtd2l0aC1BRVMyNTYtIiwicmVxdWVzdF9pZCI6IkNDQTc6MzI1NDc0OjIxMThDMDU6MjE2Nzg1MDo2NUNBNUYxMiIsInZpc2l0b3JfaWQiOiI1ODc3NDI2MzIxMjE4MjM4OTE4IiwicmVnaW9uX2VkZ2UiOiJmcmEiLCJyZWdpb25fcmVuZGVyIjoiaWFkIn0=" data-turbo-transient="true"><meta name="visitor-hmac" content="fe27226345d8be32c063efec100ca9d82c6440e6f2458dd03c9bf82431bd2981" data-turbo-transient="true"><meta name="hovercard-subject-tag" content="repository:614408864" data-turbo-transient=""><meta name="github-keyboard-shortcuts" content="repository,source-code,file-tree,copilot" data-turbo-transient="true"><meta name="selected-link" value="repo_source" data-turbo-transient=""><link rel="assets" href="https://github.githubassets.com/"><meta name="google-site-verification" content="c1kuD-K2HIVF635lypcsWPoD4kilo5-jA_wBFyT4uMY"><meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU"><meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA"><meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc"><meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I"><meta name="octolytics-url" content="https://collector.github.com/github/collect"><meta name="octolytics-actor-id" content="97131465"><meta name="octolytics-actor-login" content="Mo23fathi"><meta name="octolytics-actor-hash" content="05b5326eea5ad211686cb0b62023e21f340ca8b8787e902dfc72fef8f447b00b"><meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-turbo-transient="true"><meta name="user-login" content="Mo23fathi"><link rel="sudo-modal" href="https://github.com/sessions/sudo_modal"><meta name="turbo-cache-control" content="no-preview" data-turbo-transient=""><meta name="turbo-cache-control" content="no-cache" data-turbo-transient=""><meta data-hydrostats="publish"><meta name="go-import" content="github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256- git https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-.git"><meta name="octolytics-dimension-user_id" content="106034331"><meta name="octolytics-dimension-user_login" content="helmii18"><meta name="octolytics-dimension-repository_id" content="614408864"><meta name="octolytics-dimension-repository_nwo" content="helmii18/encrypt-decrypt-pdf-file-with-AES256-"><meta name="octolytics-dimension-repository_public" content="true"><meta name="octolytics-dimension-repository_is_fork" content="false"><meta name="octolytics-dimension-repository_network_root_id" content="614408864"><meta name="octolytics-dimension-repository_network_root_nwo" content="helmii18/encrypt-decrypt-pdf-file-with-AES256-"><meta name="turbo-body-classes" content="logged-in env-production page-responsive"><meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats"><meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors"><link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000"><link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon-dark.png"><link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon-dark.svg"><meta name="theme-color" content="#1e2327"><meta name="color-scheme" content="light dark"><link rel="manifest" href="https://github.com/manifest.json" crossorigin="use-credentials"><style type="text/css" id="ms-consent-banner-theme-styles"></style></head>

  <body class="logged-in env-production page-responsive intent-mouse" style="overflow-wrap: break-word; --dialog-scrollgutter: 17px;">
    <div data-turbo-body="" class="logged-in env-production page-responsive" style="word-wrap: break-word;">
      


    <div class="position-relative js-header-wrapper ">
      <a href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/blob/main/AES256.py#start-of-content" class="p-3 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>
      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      
  




<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_primer_react_lib-esm_Button_IconButton_js-node_modules_primer_react_lib--23bcad-ccf1d5fc6054.js.download"></script>

<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/keyboard-shortcuts-dialog-a2ca669523db.js.download"></script>

<react-partial partial-name="keyboard-shortcuts-dialog" data-ssr="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{}}</script>
  <div data-target="react-partial.reactRoot"><script type="application/json" id="__PRIMER_DATA__">{"resolvedServerColorMode":"night"}</script></div>
</react-partial>



      

        <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_allex_crc32_lib_crc32_esm_js-node_modules_github_mini-throttle_dist_deco-b38cad-748e74df23ce.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/vendors-node_modules_github_clipboard-copy-element_dist_index_esm_js-node_modules_delegated-e-b37f7d-2f24d321a3fb.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/app_assets_modules_github_command-palette_items_help-item_ts-app_assets_modules_github_comman-48ad9d-2eb78c4e07c5.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/command-palette-4a91d9475ff6.js.download"></script>

            <header class="AppHeader">
    

    <div class="AppHeader-globalBar pb-2 js-global-bar">
      <div class="AppHeader-globalBar-start">
          <deferred-side-panel data-url="/_side-panels/global" data-catalyst="">
  <include-fragment data-target="deferred-side-panel.fragment"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
      <button aria-label="Open global navigation menu" data-action="click:deferred-side-panel#loadPanel click:deferred-side-panel#panelOpened" data-show-dialog-id="dialog-1a913930-892e-4342-8a33-94e6d213a773" id="dialog-show-dialog-1a913930-892e-4342-8a33-94e6d213a773" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-bg-transparent p-0 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-three-bars Button-visual">
    <path d="M1 2.75A.75.75 0 0 1 1.75 2h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 2.75Zm0 5A.75.75 0 0 1 1.75 7h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 7.75ZM1.75 12h12.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Z"></path>
</svg>
</button>

<dialog-helper>
  <dialog data-target="deferred-side-panel.panel" id="dialog-1a913930-892e-4342-8a33-94e6d213a773" aria-modal="true" aria-disabled="true" aria-labelledby="dialog-1a913930-892e-4342-8a33-94e6d213a773-title" aria-describedby="dialog-1a913930-892e-4342-8a33-94e6d213a773-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait Overlay--motion-scaleFade Overlay--placement-left SidePanel">
    <div styles="flex-direction: row;" data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title sr-only" id="dialog-1a913930-892e-4342-8a33-94e6d213a773-title">
        Global navigation
      </h1>
            <div data-view-component="true" class="d-flex">
      <div data-view-component="true" class="AppHeader-logo position-relative">
        <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
</div></div>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="dialog-1a913930-892e-4342-8a33-94e6d213a773" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <scrollable-region data-labelled-by="dialog-1a913930-892e-4342-8a33-94e6d213a773-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body d-flex flex-column px-2">    <div data-view-component="true" class="d-flex flex-column mb-3">
        <nav aria-label="Site navigation" data-view-component="true" class="ActionList">
  
  <nav-list data-catalyst="">
    <ul data-view-component="true" class="ActionListWrap">
        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-hotkey="g d" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;HOME&quot;,&quot;label&quot;:null}" id="item-46469f20-0f29-4fe9-a8e7-bf5175d03efb" href="https://github.com/dashboard" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-home">
    <path d="M6.906.664a1.749 1.749 0 0 1 2.187 0l5.25 4.2c.415.332.657.835.657 1.367v7.019A1.75 1.75 0 0 1 13.25 15h-3.5a.75.75 0 0 1-.75-.75V9H7v5.25a.75.75 0 0 1-.75.75h-3.5A1.75 1.75 0 0 1 1 13.25V6.23c0-.531.242-1.034.657-1.366l5.25-4.2Zm1.25 1.171a.25.25 0 0 0-.312 0l-5.25 4.2a.25.25 0 0 0-.094.196v7.019c0 .138.112.25.25.25H5.5V8.25a.75.75 0 0 1 .75-.75h3.5a.75.75 0 0 1 .75.75v5.25h2.75a.25.25 0 0 0 .25-.25V6.23a.25.25 0 0 0-.094-.195Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Home
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES&quot;,&quot;label&quot;:null}" id="item-e772283e-4d43-4be1-82a5-b39e79be03d0" href="https://github.com/issues" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS&quot;,&quot;label&quot;:null}" id="item-0ccf16be-bd96-41bb-9274-0855a28ba890" href="https://github.com/pulls" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PROJECTS&quot;,&quot;label&quot;:null}" id="item-8bc69e9e-27a1-4b3e-bde8-dd65814e3655" href="https://github.com/projects" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;DISCUSSIONS&quot;,&quot;label&quot;:null}" id="item-f9926d00-b61c-46a7-a201-40eab1a456ef" href="https://github.com/discussions" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-comment-discussion">
    <path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Discussions
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;CODESPACES&quot;,&quot;label&quot;:null}" id="item-470e025d-1950-40bf-9369-a4fde6613db4" href="https://github.com/codespaces" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Codespaces
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;EXPLORE&quot;,&quot;label&quot;:null}" id="item-057020b1-f282-4770-9525-1389b0b56bfc" href="https://github.com/explore" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-telescope">
    <path d="M14.184 1.143v-.001l1.422 2.464a1.75 1.75 0 0 1-.757 2.451L3.104 11.713a1.75 1.75 0 0 1-2.275-.702l-.447-.775a1.75 1.75 0 0 1 .53-2.32L11.682.573a1.748 1.748 0 0 1 2.502.57Zm-4.709 9.32h-.001l2.644 3.863a.75.75 0 1 1-1.238.848l-1.881-2.75v2.826a.75.75 0 0 1-1.5 0v-2.826l-1.881 2.75a.75.75 0 1 1-1.238-.848l2.049-2.992a.746.746 0 0 1 .293-.253l1.809-.87a.749.749 0 0 1 .944.252ZM9.436 3.92h-.001l-4.97 3.39.942 1.63 5.42-2.61Zm3.091-2.108h.001l-1.85 1.26 1.505 2.605 2.016-.97a.247.247 0 0 0 .13-.151.247.247 0 0 0-.022-.199l-1.422-2.464a.253.253 0 0 0-.161-.119.254.254 0 0 0-.197.038ZM1.756 9.157a.25.25 0 0 0-.075.33l.447.775a.25.25 0 0 0 .325.1l1.598-.769-.83-1.436-1.465 1Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Explore
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;MARKETPLACE&quot;,&quot;label&quot;:null}" id="item-ff2a8124-0d9c-4024-b233-880e2221fe9a" href="https://github.com/marketplace" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gift">
    <path d="M2 2.75A2.75 2.75 0 0 1 4.75 0c.983 0 1.873.42 2.57 1.232.268.318.497.668.68 1.042.183-.375.411-.725.68-1.044C9.376.42 10.266 0 11.25 0a2.75 2.75 0 0 1 2.45 4h.55c.966 0 1.75.784 1.75 1.75v2c0 .698-.409 1.301-1 1.582v4.918A1.75 1.75 0 0 1 13.25 16H2.75A1.75 1.75 0 0 1 1 14.25V9.332C.409 9.05 0 8.448 0 7.75v-2C0 4.784.784 4 1.75 4h.55c-.192-.375-.3-.8-.3-1.25ZM7.25 9.5H2.5v4.75c0 .138.112.25.25.25h4.5Zm1.5 0v5h4.5a.25.25 0 0 0 .25-.25V9.5Zm0-4V8h5.5a.25.25 0 0 0 .25-.25v-2a.25.25 0 0 0-.25-.25Zm-7 0a.25.25 0 0 0-.25.25v2c0 .138.112.25.25.25h5.5V5.5h-5.5Zm3-4a1.25 1.25 0 0 0 0 2.5h2.309c-.233-.818-.542-1.401-.878-1.793-.43-.502-.915-.707-1.431-.707ZM8.941 4h2.309a1.25 1.25 0 0 0 0-2.5c-.516 0-1 .205-1.43.707-.337.392-.646.975-.879 1.793Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Marketplace
</span></a>
  
  
</li>

</ul>  </nav-list>
</nav>

        <div data-view-component="true" class="my-3 d-flex flex-justify-center height-full">
          <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
</div>
</div>
      <div data-view-component="true" class="flex-1"></div>


      <div data-view-component="true" class="px-2">      <p class="color-fg-subtle text-small text-light">© 2024 GitHub, Inc.</p>

      <div data-view-component="true" class="d-flex flex-wrap text-small text-light">
          <a target="_blank" href="https://github.com/about" data-view-component="true" class="Link mr-2">About</a>
          <a target="_blank" href="https://github.blog/" data-view-component="true" class="Link mr-2">Blog</a>
          <a target="_blank" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link mr-2">Terms</a>
          <a target="_blank" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link mr-2">Privacy</a>
          <a target="_blank" href="https://github.com/security" data-view-component="true" class="Link mr-2">Security</a>
          <a target="_blank" href="https://www.githubstatus.com/" data-view-component="true" class="Link mr-3">Status</a>

</div></div>
</div>
      </scrollable-region>
      
</dialog></dialog-helper>

  </include-fragment>
</deferred-side-panel>

        <a class="AppHeader-logo ml-2" href="https://github.com/" data-hotkey="g d" aria-label="Homepage " data-turbo="false" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;}">
          <svg height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle color-fg-default">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
        </a>

          <div class="AppHeader-context">
  <div class="AppHeader-context-compact">
      <button aria-expanded="false" aria-haspopup="dialog" aria-label="Page context: helmii18 / encrypt-decrypt-pdf-file-with-AES256-" id="dialog-show-context-region-dialog" data-show-dialog-id="context-region-dialog" type="button" data-view-component="true" class="AppHeader-context-compact-trigger Truncate Button--secondary Button--medium Button box-shadow-none">  <span class="Button-content">
    <span class="Button-label"><span class="AppHeader-context-compact-lead">
                <span class="AppHeader-context-compact-parentItem">helmii18</span>
                <span class="no-wrap">&nbsp;/</span>

            </span>

            <strong class="AppHeader-context-compact-mainItem d-flex flex-items-center Truncate">
  <span class="Truncate-text ">encrypt-decrypt-pdf-file-with-AES256-</span>

</strong></span>
  </span>
</button>

<dialog-helper>
  <dialog id="context-region-dialog" aria-modal="true" aria-disabled="true" aria-labelledby="context-region-dialog-title" aria-describedby="context-region-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="context-region-dialog-title">
        Navigate back to
      </h1>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="context-region-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <scrollable-region data-labelled-by="context-region-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">          <ul role="list" class="list-style-none">
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;helmii18&quot;,&quot;screen_size&quot;:&quot;compact&quot;}" href="https://github.com/helmii18" data-view-component="true" class="Link--primary Truncate d-flex flex-items-center py-1">
        <span class="AppHeader-context-item-label Truncate-text ">
            <svg aria-hidden="true" height="12" viewBox="0 0 16 16" version="1.1" width="12" data-view-component="true" class="octicon octicon-person mr-1">
    <path d="M10.561 8.073a6.005 6.005 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07 4.5 4.5 0 0 0-8.99 0 .75.75 0 0 1-1.498-.07 6.004 6.004 0 0 1 3.431-5.142 3.999 3.999 0 1 1 5.123 0ZM10.5 5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path>
</svg>

          helmii18
        </span>

</a>
    </li>
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;encrypt-decrypt-pdf-file-with-AES256-&quot;,&quot;screen_size&quot;:&quot;compact&quot;}" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-" data-view-component="true" class="Link--primary Truncate d-flex flex-items-center py-1">
        <span class="AppHeader-context-item-label Truncate-text ">
            <svg aria-hidden="true" height="12" viewBox="0 0 16 16" version="1.1" width="12" data-view-component="true" class="octicon octicon-repo mr-1">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>

          encrypt-decrypt-pdf-file-with-AES256-
        </span>

</a>
    </li>
</ul>

</div>
      </scrollable-region>
      
</dialog></dialog-helper>
  </div>

  <div class="AppHeader-context-full">
    <nav role="navigation" aria-label="Page context">
      <ul role="list" class="list-style-none">
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;helmii18&quot;,&quot;screen_size&quot;:&quot;full&quot;}" data-hovercard-type="user" data-hovercard-url="/users/helmii18/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/helmii18" data-view-component="true" class="AppHeader-context-item">
        <span class="AppHeader-context-item-label  ">

          helmii18
        </span>

</a>
        <span class="AppHeader-context-item-separator">/</span>
    </li>
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;encrypt-decrypt-pdf-file-with-AES256-&quot;,&quot;screen_size&quot;:&quot;full&quot;}" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-" data-view-component="true" class="AppHeader-context-item">
        <span class="AppHeader-context-item-label  ">

          encrypt-decrypt-pdf-file-with-AES256-
        </span>

</a>
    </li>
</ul>

    </nav>
  </div>
</div>

      </div>
      <div class="AppHeader-globalBar-end">
          <div class="AppHeader-search">
              


<qbsearch-input class="search-input" data-scope="repo:helmii18/encrypt-decrypt-pdf-file-with-AES256-" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="rBSFYChRQu2wFzi58twfxhIHpgQ1AxhvTG98PDA7EUo9j3MtF1DDeYMw3l4A-hFX-aEirQlwiYPRi1ogYB9Kig" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="helmii18/encrypt-decrypt-pdf-file-with-AES256-" data-current-org="" data-current-owner="helmii18" data-logged-in="true" data-copilot-chat-enabled="false" data-blackbird-indexed-repo-csrf="&lt;input type=&quot;hidden&quot; value=&quot;etE2iPNt8RXCLfEEVi1VNR1BrvgpMK8TpzWUmPEvL4Q3crIhAsWZLAgwQ-e5dkofnENVyv6QbzDV8VaArAyWAg&quot; data-csrf=&quot;true&quot; /&gt;" data-catalyst="">
  <div class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0" data-action="click:qbsearch-input#searchInputContainerClicked">
      
            <button type="button" data-action="click:qbsearch-input#handleExpand" class="AppHeader-button AppHeader-search-whenNarrow" aria-label="Search or jump to…" aria-expanded="false" aria-haspopup="dialog">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </button>


<div class="AppHeader-search-whenRegular">
  <div class="AppHeader-search-wrap AppHeader-search-wrap--hasTrailing">
    <div class="AppHeader-search-control">
      <label for="AppHeader-searchInput" aria-label="Search or jump to…" class="AppHeader-search-visual--leading">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
      </label>

                <button type="button" data-target="qbsearch-input.inputButton" data-action="click:qbsearch-input#handleExpand" class="AppHeader-searchButton form-control input-contrast text-left color-fg-subtle no-wrap placeholder" data-hotkey="s,/" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;SEARCH&quot;,&quot;label&quot;:null}">
            <div class="overflow-hidden">
              <span id="qb-input-query" data-target="qbsearch-input.inputButtonText">
                  Type <kbd class="AppHeader-search-kbd">/</kbd> to search
              </span>
            </div>
          </button>

    </div>


      <button type="button" id="AppHeader-commandPalette-button" class="AppHeader-search-action--trailing js-activate-command-palette" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;command_palette&quot;,&quot;label&quot;:&quot;open command palette&quot;}" aria-labelledby="tooltip-94c0ed59-de10-48af-b5c4-29e094240e0d">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-command-palette">
    <path d="m6.354 8.04-4.773 4.773a.75.75 0 1 0 1.061 1.06L7.945 8.57a.75.75 0 0 0 0-1.06L2.642 2.206a.75.75 0 0 0-1.06 1.061L6.353 8.04ZM8.75 11.5a.75.75 0 0 0 0 1.5h5.5a.75.75 0 0 0 0-1.5h-5.5Z"></path>
</svg>
      </button>

      <tool-tip id="tooltip-94c0ed59-de10-48af-b5c4-29e094240e0d" for="AppHeader-commandPalette-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tool-tip-position-top, 0) auto auto var(--tool-tip-position-left, 0) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
        content: "";
        border: 6px solid transparent;
        opacity: 0;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: "";
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open),
      :host(.\:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }
      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }
      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }
      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }
      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }
      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Command palette</tool-tip>
  </div>
</div>

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay="">
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container" style="border-radius: 12px;" data-target="qbsearch-input.queryBuilderContainer" hidden="">
          <!-- '"` --><!-- </textarea></xmp> --><form id="query-builder-test-form" action="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/blob/main/AES256.py" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder" data-min-width="300" data-catalyst="">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div class="QueryBuilder-StyledInput width-fit " data-target="query-builder.styledInput">
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div aria-hidden="true" class="QueryBuilder-StyledInputContent" data-target="query-builder.styledInputContent"></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"><span></span></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-f2dd06de-416e-4683-8f7e-af67acd4ef3d" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" aria-controls="query-builder-test-results" aria-autocomplete="list" aria-haspopup="listbox" style="width: 300px;">
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

      </div>
      <template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

<template id="copilot-icon"></template>

        <div class="position-relative">
                <ul role="listbox" class="ActionListWrap QueryBuilder-ListWrap" aria-label="Suggestions" data-action="
                    combobox-commit:query-builder#comboboxCommit
                    mousedown:query-builder#resultsMousedown
                  " data-target="query-builder.resultsList" data-persist-list="false" id="query-builder-test-results"></ul>
        </div>
      <div class="FormControl-inlineValidation" id="validation-f2dd06de-416e-4683-8f7e-af67acd4ef3d" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only">0 suggestions.</div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">
              Search syntax tips
</a>            <div class="d-flex flex-1"></div>
              <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2">  <span class="Button-content">
    <span class="Button-label">Give feedback</span>
  </span>
</button>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden="" data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-disabled="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --><form id="code-search-feedback-form" data-turbo="false" action="https://github.com/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="RXuf0HO7BUo6495CtNt6_AFOia7DpMSjZvCjUsiclz8cr24ulmfP68T0HahAAKoaLUeDipBuZq7fRPM1zGl2sw">
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager" data-catalyst="">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-disabled="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden="" class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --><form id="custom-scopes-dialog-form" data-turbo="false" action="https://github.com/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="6Oa8pVJt9rueeyM1q6ceEogdMD-Z7myyA0GO3YfzrClCyud9uPgXcU2UGrA4mQUgFUVPNUrqlLVrsX4FG1dJPQ">
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required="">
              <input type="text" name="custom_scope_name" id="custom_scope_name" data-target="custom-scopes.customScopesNameField" class="form-control" autocomplete="off" placeholder="github-ruby" required="" maxlength="50" spellcheck="false">
              <input type="hidden" value="TqFOUNbvvnKziIHA9MeJ8zXTCqS8_b31tKZCXUj-RoorCQxZySzsn7ss3-1AcMngabZxjqAgzZ_LXZG3MENLdg" data-csrf="true">
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input type="text" name="custom_scope_query" id="custom_scope_query" data-target="custom-scopes.customScopesQueryField" class="form-control" autocomplete="off" placeholder="(repo:mona/a OR repo:mona/b) AND lang:python" required="" maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input><input type="hidden" value="1criAQ499aiq6DFsuHTBvI9Xo2bXi4y_PJaFFFYgEIVkDUO-Mvx15ZZixXaVOzFJAZjEukLzA1NKafFK7DwUdA" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf">

          </div>

        <div class="AppHeader-actions position-relative">
          <action-menu data-select-variant="none" data-view-component="true" data-catalyst="">
  <focus-group direction="vertical" mnemonics="" retain="">
    <button id="global-create-menu-button" popovertarget="global-create-menu-overlay" aria-label="Create something new" aria-controls="global-create-menu-list" aria-haspopup="true" type="button" data-view-component="true" class="AppHeader-button Button--secondary Button--small Button width-auto color-fg-muted" aria-describedby="tooltip-6e50dbd1-1059-4c37-a14c-9b19d5c2637e">  <span class="Button-content">
      <span class="Button-visual Button-leadingVisual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
      </span>
    <span class="Button-label"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg></span>
  </span>
</button><tool-tip id="tooltip-6e50dbd1-1059-4c37-a14c-9b19d5c2637e" for="global-create-menu-button" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tool-tip-position-top, 0) auto auto var(--tool-tip-position-left, 0) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
        content: "";
        border: 6px solid transparent;
        opacity: 0;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: "";
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open),
      :host(.\:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }
      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }
      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }
      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }
      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }
      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Create new...</tool-tip>


<anchored-position id="global-create-menu-overlay" anchor="global-create-menu-button" align="end" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true" style="inset: 36px auto auto 70.6px;">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <div data-view-component="true">
  <ul aria-labelledby="global-create-menu-button" id="global-create-menu-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new repository&quot;}" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://github.com/new" tabindex="-1" id="item-d095e783-13d3-4a9e-ab40-7eb203b71599" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
              New repository

</span></a>
  
  
</li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;import repository&quot;}" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://github.com/new/import" tabindex="-1" id="item-b84aa40e-5534-4ef5-9bca-6c7c1dfba83c" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-push">
    <path d="M1 2.5A2.5 2.5 0 0 1 3.5 0h8.75a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0V1.5h-8a1 1 0 0 0-1 1v6.708A2.493 2.493 0 0 1 3.5 9h3.25a.75.75 0 0 1 0 1.5H3.5a1 1 0 0 0 0 2h5.75a.75.75 0 0 1 0 1.5H3.5A2.5 2.5 0 0 1 1 11.5Zm13.23 7.79h-.001l-1.224-1.224v6.184a.75.75 0 0 1-1.5 0V9.066L10.28 10.29a.75.75 0 0 1-1.06-1.061l2.505-2.504a.75.75 0 0 1 1.06 0L15.29 9.23a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                Import repository

</span></a>
  
  
</li>
      <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new codespace&quot;}" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://github.com/codespaces/new" tabindex="-1" id="item-94a91ee0-858e-452e-8baa-ee459567786f" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New codespace

</span></a>
  
  
</li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new gist&quot;}" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://gist.github.com/" tabindex="-1" id="item-0ef29e7d-6baf-4ec2-890f-64c571022ea3" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New gist

</span></a>
  
  
</li>
      <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
      <li data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://github.com/account/organizations/new" tabindex="-1" data-dont-follow-via-test="true" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new organization&quot;}" id="item-20e54411-03c2-4bd5-8327-36719a7e1220" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-organization">
    <path d="M1.75 16A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0h8.5C11.216 0 12 .784 12 1.75v12.5c0 .085-.006.168-.018.25h2.268a.25.25 0 0 0 .25-.25V8.285a.25.25 0 0 0-.111-.208l-1.055-.703a.749.749 0 1 1 .832-1.248l1.055.703c.487.325.779.871.779 1.456v5.965A1.75 1.75 0 0 1 14.25 16h-3.5a.766.766 0 0 1-.197-.026c-.099.017-.2.026-.303.026h-3a.75.75 0 0 1-.75-.75V14h-1v1.25a.75.75 0 0 1-.75.75Zm-.25-1.75c0 .138.112.25.25.25H4v-1.25a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 .75.75v1.25h2.25a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25ZM3.75 6h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 3.75A.75.75 0 0 1 3.75 3h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 3.75Zm4 3A.75.75 0 0 1 7.75 6h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 7 6.75ZM7.75 3h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 9.75A.75.75 0 0 1 3.75 9h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 9.75ZM7.75 9h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New organization

</span></a>
  
  
</li>
</ul>  
</div>

</div>
      
</div></anchored-position>  </focus-group>
</action-menu>


          <a href="https://github.com/issues" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-71546112-03f0-4bb4-8424-ccf085ba7e11" aria-labelledby="tooltip-db8c4995-9e9b-4a6a-b044-1d4170b5736b" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened Button-visual">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
</a><tool-tip id="tooltip-db8c4995-9e9b-4a6a-b044-1d4170b5736b" for="icon-button-71546112-03f0-4bb4-8424-ccf085ba7e11" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tool-tip-position-top, 0) auto auto var(--tool-tip-position-left, 0) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
        content: "";
        border: 6px solid transparent;
        opacity: 0;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: "";
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open),
      :host(.\:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }
      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }
      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }
      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }
      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }
      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Issues</tool-tip>

          <a href="https://github.com/pulls" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-fa7d02aa-064c-4494-84d6-9e89fa90656e" aria-labelledby="tooltip-ec2fdc8f-a9ed-440a-abc7-70197966ec14" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request Button-visual">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
</a><tool-tip id="tooltip-ec2fdc8f-a9ed-440a-abc7-70197966ec14" for="icon-button-fa7d02aa-064c-4494-84d6-9e89fa90656e" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tool-tip-position-top, 0) auto auto var(--tool-tip-position-left, 0) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
        content: "";
        border: 6px solid transparent;
        opacity: 0;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: "";
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open),
      :host(.\:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }
      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }
      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }
      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }
      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }
      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Pull requests</tool-tip>

        </div>

        
<notification-indicator data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6OTcxMzE0NjUiLCJ0IjoxNzA3NzYxNDI5fQ==--7e25fde7943992c5e2112765c3f979ac496e3b3e93866882b3f4c0ca5bec1e67" data-indicator-mode="none" data-tooltip-global="You have unread notifications" data-tooltip-unavailable="Notifications are unavailable at the moment." data-tooltip-none="You have no unread notifications" data-header-redesign-enabled="true" data-fetch-indicator-src="/notifications/indicator" data-fetch-indicator-enabled="true" data-view-component="true" class="js-socket-channel" data-fetch-retry-delay-time="500" data-catalyst="">
    <a id="AppHeader-notifications-button" href="https://github.com/notifications" aria-label="Notifications" data-hotkey="g n" data-target="notification-indicator.link" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;NOTIFICATIONS_HEADER&quot;,&quot;label&quot;:&quot;icon:read&quot;}" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted" aria-describedby="tooltip-c29fb3f9-9de6-4719-a9b0-4b6e93055c52">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-inbox Button-visual">
    <path d="M2.8 2.06A1.75 1.75 0 0 1 4.41 1h7.18c.7 0 1.333.417 1.61 1.06l2.74 6.395c.04.093.06.194.06.295v4.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25v-4.5c0-.101.02-.202.06-.295Zm1.61.44a.25.25 0 0 0-.23.152L1.887 8H4.75a.75.75 0 0 1 .6.3L6.625 10h2.75l1.275-1.7a.75.75 0 0 1 .6-.3h2.863L11.82 2.652a.25.25 0 0 0-.23-.152Zm10.09 7h-2.875l-1.275 1.7a.75.75 0 0 1-.6.3h-3.5a.75.75 0 0 1-.6-.3L4.375 9.5H1.5v3.75c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Z"></path>
</svg>
</a>

    <tool-tip data-target="notification-indicator.tooltip" id="tooltip-c29fb3f9-9de6-4719-a9b0-4b6e93055c52" for="AppHeader-notifications-button" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tool-tip-position-top, 0) auto auto var(--tool-tip-position-left, 0) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
        content: "";
        border: 6px solid transparent;
        opacity: 0;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: "";
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open),
      :host(.\:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }
      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }
      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }
      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }
      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }
      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>You have no unread notifications</tool-tip>
</notification-indicator>

        

        <div class="AppHeader-user">
          <deferred-side-panel data-url="/_side-panels/user?repository_id=614408864" data-catalyst="">
  <include-fragment data-target="deferred-side-panel.fragment"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
      <user-drawer-side-panel data-catalyst="">
    <button aria-label="Open user account menu" data-action="click:deferred-side-panel#loadPanel click:deferred-side-panel#panelOpened" data-show-dialog-id="dialog-8248f091-b836-4fa0-a6ff-df18dc3f1d38" id="dialog-show-dialog-8248f091-b836-4fa0-a6ff-df18dc3f1d38" type="button" data-view-component="true" class="AppHeader-logo Button--invisible Button--medium Button Button--invisible-noVisuals color-bg-transparent p-0">  <span class="Button-content">
    <span class="Button-label"><img src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/97131465" alt="" size="32" height="32" width="32" data-view-component="true" class="avatar circle"></span>
  </span>
</button>

<dialog-helper>
  <dialog data-target="deferred-side-panel.panel" id="dialog-8248f091-b836-4fa0-a6ff-df18dc3f1d38" aria-modal="true" aria-disabled="true" aria-labelledby="dialog-8248f091-b836-4fa0-a6ff-df18dc3f1d38-title" aria-describedby="dialog-8248f091-b836-4fa0-a6ff-df18dc3f1d38-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait Overlay--motion-scaleFade Overlay--placement-right SidePanel">
    <div styles="flex-direction: row;" data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title sr-only" id="dialog-8248f091-b836-4fa0-a6ff-df18dc3f1d38-title">
        Account menu
      </h1>
            <div data-view-component="true" class="d-flex">
      <div data-view-component="true" class="AppHeader-logo position-relative">
        <img src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/97131465" alt="" size="32" height="32" width="32" data-view-component="true" class="avatar circle">
</div>        <div data-view-component="true" class="overflow-hidden d-flex width-full">        <div data-view-component="true" class="lh-condensed overflow-hidden d-flex flex-column flex-justify-center ml-2 f5 mr-auto width-full">
          <span data-view-component="true" class="Truncate text-bold">
    <span data-view-component="true" class="Truncate-text">
            Mo23fathi
</span>
</span>          </div>
        <action-menu data-select-variant="none" data-view-component="true" class="d-sm-none d-md-none d-lg-none" data-catalyst="">
  <focus-group direction="vertical" mnemonics="" retain="">
    <button id="user-create-menu-button" popovertarget="user-create-menu-overlay" aria-label="Create something new" aria-controls="user-create-menu-list" aria-haspopup="true" type="button" data-view-component="true" class="AppHeader-button Button--secondary Button--small Button width-auto color-fg-muted" aria-describedby="tooltip-92b6c905-bf48-4624-bdf6-d059bb4d83c0">  <span class="Button-content">
      <span class="Button-visual Button-leadingVisual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
      </span>
    <span class="Button-label"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg></span>
  </span>
</button><tool-tip id="tooltip-92b6c905-bf48-4624-bdf6-d059bb4d83c0" for="user-create-menu-button" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tool-tip-position-top, 0) auto auto var(--tool-tip-position-left, 0) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
        content: "";
        border: 6px solid transparent;
        opacity: 0;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: "";
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open),
      :host(.\:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }
      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }
      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }
      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }
      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }
      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Create new...</tool-tip>


<anchored-position id="user-create-menu-overlay" anchor="user-create-menu-button" align="end" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true" style="inset: 4px auto auto 0px;">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <div data-view-component="true">
  <ul aria-labelledby="user-create-menu-button" id="user-create-menu-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new repository&quot;}" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://github.com/new" tabindex="-1" id="item-3f92c932-a8fd-4959-ac55-b5667648b1c4" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
              New repository

</span></a>
  
  
</li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;import repository&quot;}" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://github.com/new/import" tabindex="-1" id="item-02875fc7-7557-4ee1-a728-1e9a014f4c36" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-push">
    <path d="M1 2.5A2.5 2.5 0 0 1 3.5 0h8.75a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0V1.5h-8a1 1 0 0 0-1 1v6.708A2.493 2.493 0 0 1 3.5 9h3.25a.75.75 0 0 1 0 1.5H3.5a1 1 0 0 0 0 2h5.75a.75.75 0 0 1 0 1.5H3.5A2.5 2.5 0 0 1 1 11.5Zm13.23 7.79h-.001l-1.224-1.224v6.184a.75.75 0 0 1-1.5 0V9.066L10.28 10.29a.75.75 0 0 1-1.06-1.061l2.505-2.504a.75.75 0 0 1 1.06 0L15.29 9.23a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                Import repository

</span></a>
  
  
</li>
      <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new codespace&quot;}" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://github.com/codespaces/new" tabindex="-1" id="item-008a14b3-7c9f-437c-b666-84c8a85d4d80" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New codespace

</span></a>
  
  
</li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new gist&quot;}" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://gist.github.com/" tabindex="-1" id="item-af99d741-9e82-4e41-90ab-5d69030d8282" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New gist

</span></a>
  
  
</li>
      <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
      <li data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://github.com/account/organizations/new" tabindex="-1" data-dont-follow-via-test="true" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new organization&quot;}" id="item-49c18022-3a2b-4a82-a627-2416663f122e" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-organization">
    <path d="M1.75 16A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0h8.5C11.216 0 12 .784 12 1.75v12.5c0 .085-.006.168-.018.25h2.268a.25.25 0 0 0 .25-.25V8.285a.25.25 0 0 0-.111-.208l-1.055-.703a.749.749 0 1 1 .832-1.248l1.055.703c.487.325.779.871.779 1.456v5.965A1.75 1.75 0 0 1 14.25 16h-3.5a.766.766 0 0 1-.197-.026c-.099.017-.2.026-.303.026h-3a.75.75 0 0 1-.75-.75V14h-1v1.25a.75.75 0 0 1-.75.75Zm-.25-1.75c0 .138.112.25.25.25H4v-1.25a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 .75.75v1.25h2.25a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25ZM3.75 6h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 3.75A.75.75 0 0 1 3.75 3h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 3.75Zm4 3A.75.75 0 0 1 7.75 6h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 7 6.75ZM7.75 3h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 9.75A.75.75 0 0 1 3.75 9h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 9.75ZM7.75 9h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New organization

</span></a>
  
  
</li>
</ul>  
</div>

</div>
      
</div></anchored-position>  </focus-group>
</action-menu>

</div>
</div>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="dialog-8248f091-b836-4fa0-a6ff-df18dc3f1d38" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <scrollable-region data-labelled-by="dialog-8248f091-b836-4fa0-a6ff-df18dc3f1d38-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body d-flex flex-column px-2">    <div data-view-component="true" class="d-flex flex-column mb-3">
        <nav aria-label="User navigation" data-view-component="true" class="ActionList">
  
  <nav-list data-catalyst="">
    <ul data-view-component="true" class="ActionListWrap">
        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <button id="item-2ad36f8b-1087-44a5-a3af-4fc66f701179" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PROFILE&quot;,&quot;label&quot;:null}" id="item-2abecbae-6750-4d1e-9400-ea934620b5a0" href="https://github.com/Mo23fathi" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-person">
    <path d="M10.561 8.073a6.005 6.005 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07 4.5 4.5 0 0 0-8.99 0 .75.75 0 0 1-1.498-.07 6.004 6.004 0 0 1 3.431-5.142 3.999 3.999 0 1 1 5.123 0ZM10.5 5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your profile
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <button id="item-cbb48f70-2970-42e0-bd85-b312cd0d79e8" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;YOUR_REPOSITORIES&quot;,&quot;label&quot;:null}" id="item-b7ae8d8c-cd31-4fa7-9d3d-fbdc601e48f4" href="https://github.com/Mo23fathi?tab=repositories" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your repositories
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;YOUR_PROJECTS&quot;,&quot;label&quot;:null}" id="item-232d2a97-ce5b-4bea-a0cc-45d03c5d0c46" href="https://github.com/Mo23fathi?tab=projects" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project">
    <path d="M1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0ZM1.5 1.75v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25ZM11.75 3a.75.75 0 0 1 .75.75v7.5a.75.75 0 0 1-1.5 0v-7.5a.75.75 0 0 1 .75-.75Zm-8.25.75a.75.75 0 0 1 1.5 0v5.5a.75.75 0 0 1-1.5 0ZM8 3a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 3Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your projects
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <button id="item-a16971b4-d484-475d-a694-719c1122ddac" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;YOUR_STARS&quot;,&quot;label&quot;:null}" id="item-badb7156-1902-4a4b-977c-d77073578688" href="https://github.com/Mo23fathi?tab=stars" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your stars
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;SPONSORS&quot;,&quot;label&quot;:null}" id="item-ac0ce217-47d3-4244-bbe9-4bba9a9c7329" href="https://github.com/sponsors/accounts" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-heart">
    <path d="m8 14.25.345.666a.75.75 0 0 1-.69 0l-.008-.004-.018-.01a7.152 7.152 0 0 1-.31-.17 22.055 22.055 0 0 1-3.434-2.414C2.045 10.731 0 8.35 0 5.5 0 2.836 2.086 1 4.25 1 5.797 1 7.153 1.802 8 3.02 8.847 1.802 10.203 1 11.75 1 13.914 1 16 2.836 16 5.5c0 2.85-2.045 5.231-3.885 6.818a22.066 22.066 0 0 1-3.744 2.584l-.018.01-.006.003h-.002ZM4.25 2.5c-1.336 0-2.75 1.164-2.75 3 0 2.15 1.58 4.144 3.365 5.682A20.58 20.58 0 0 0 8 13.393a20.58 20.58 0 0 0 3.135-2.211C12.92 9.644 14.5 7.65 14.5 5.5c0-1.836-1.414-3-2.75-3-1.373 0-2.609.986-3.029 2.456a.749.749 0 0 1-1.442 0C6.859 3.486 5.623 2.5 4.25 2.5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your sponsors
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;YOUR_GISTS&quot;,&quot;label&quot;:null}" id="item-145fcb66-19ca-460a-8cb3-7eaccb351cdd" href="https://gist.github.com/mine" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code-square">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25Zm7.47 3.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L10.69 8 9.22 6.53a.75.75 0 0 1 0-1.06ZM6.78 6.53 5.31 8l1.47 1.47a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your gists
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <button id="item-d36abc7b-aea8-4694-a4ca-d4bd6db59aed" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <button id="item-4abc4ca0-5921-4fcb-a04a-287a417d4f19" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <button id="item-d81edcb5-addb-4693-b409-d7ad6564d30e" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;SETTINGS&quot;,&quot;label&quot;:null}" id="item-06fd0631-6b55-4f86-ab88-07a7ab446d2c" href="https://github.com/settings/profile" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gear">
    <path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Settings
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;DOCS&quot;,&quot;label&quot;:null}" id="item-c0422925-ff90-4e97-a241-318cbd4cb9e8" href="https://docs.github.com/" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book">
    <path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          GitHub Docs
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;SUPPORT&quot;,&quot;label&quot;:null}" id="item-beb52015-598f-420a-8150-b6529a7a4379" href="https://support.github.com/" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-people">
    <path d="M2 5.5a3.5 3.5 0 1 1 5.898 2.549 5.508 5.508 0 0 1 3.034 4.084.75.75 0 1 1-1.482.235 4 4 0 0 0-7.9 0 .75.75 0 0 1-1.482-.236A5.507 5.507 0 0 1 3.102 8.05 3.493 3.493 0 0 1 2 5.5ZM11 4a3.001 3.001 0 0 1 2.22 5.018 5.01 5.01 0 0 1 2.56 3.012.749.749 0 0 1-.885.954.752.752 0 0 1-.549-.514 3.507 3.507 0 0 0-2.522-2.372.75.75 0 0 1-.574-.73v-.352a.75.75 0 0 1 .416-.672A1.5 1.5 0 0 0 11 5.5.75.75 0 0 1 11 4Zm-5.5-.5a2 2 0 1 0-.001 3.999A2 2 0 0 0 5.5 3.5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          GitHub Support
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;LOGOUT&quot;,&quot;label&quot;:null}" id="item-5c247ec0-c189-4663-b4da-a0cc77256121" href="https://github.com/logout" data-view-component="true" class="ActionListContent">
      
        <span data-view-component="true" class="ActionListItem-label">
          Sign out
</span></a>
  
  
</li>

</ul>  </nav-list>
</nav>


</div>
</div>
      </scrollable-region>
      
</dialog></dialog-helper>
  </user-drawer-side-panel>

  </include-fragment>
</deferred-side-panel>
          
        </div>

        <div class="position-absolute mt-2">
            
<site-header-logged-in-user-menu data-catalyst="">

</site-header-logged-in-user-menu>

        </div>
      </div>
    </div>


      <div class="AppHeader-localBar">
        <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /helmii18/encrypt-decrypt-pdf-file-with-AES256-" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item selected" aria-current="page">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="issues-tab" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /helmii18/encrypt-decrypt-pdf-file-with-AES256-/issues" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Issues&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        <span data-content="Issues">Issues</span>
          <span id="issues-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /helmii18/encrypt-decrypt-pdf-file-with-AES256-/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/actions" data-tab-item="i3actions-tab" data-selected-links="repo_actions /helmii18/encrypt-decrypt-pdf-file-with-AES256-/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/projects" data-tab-item="i4projects-tab" data-selected-links="repo_projects new_repo_project repo_project /helmii18/encrypt-decrypt-pdf-file-with-AES256-/projects" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Projects&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /helmii18/encrypt-decrypt-pdf-file-with-AES256-/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security">Security</span>
          

    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/pulse" data-tab-item="i6insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /helmii18/encrypt-decrypt-pdf-file-with-AES256-/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <action-menu data-select-variant="none" data-view-component="true" data-catalyst="">
  <focus-group direction="vertical" mnemonics="" retain="">
    <button id="action-menu-239bf662-8898-48bc-b8b2-a1851ef65845-button" popovertarget="action-menu-239bf662-8898-48bc-b8b2-a1851ef65845-overlay" aria-controls="action-menu-239bf662-8898-48bc-b8b2-a1851ef65845-list" aria-haspopup="true" aria-labelledby="tooltip-66c616bf-83be-49e3-b52d-205e4bce1c8c" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium UnderlineNav-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-66c616bf-83be-49e3-b52d-205e4bce1c8c" for="action-menu-239bf662-8898-48bc-b8b2-a1851ef65845-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tool-tip-position-top, 0) auto auto var(--tool-tip-position-left, 0) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
        content: "";
        border: 6px solid transparent;
        opacity: 0;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: "";
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open),
      :host(.\:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }
      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }
      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }
      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }
      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }
      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Additional navigation options</tool-tip>


<anchored-position id="action-menu-239bf662-8898-48bc-b8b2-a1851ef65845-overlay" anchor="action-menu-239bf662-8898-48bc-b8b2-a1851ef65845-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true" style="inset: 36px auto auto 0px;">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <div data-view-component="true">
  <ul aria-labelledby="action-menu-239bf662-8898-48bc-b8b2-a1851ef65845-button" id="action-menu-239bf662-8898-48bc-b8b2-a1851ef65845-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
      <li hidden="" data-menu-item="i0code-tab" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a tabindex="-1" id="item-5895ef16-c734-4ef9-9cc4-965b2e90a5fb" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Code
</span></a>
  
  
</li>
      <li hidden="" data-menu-item="i1issues-tab" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a tabindex="-1" id="item-d416c6b8-74fe-4cf8-a7fe-c0d7ee8fc042" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/issues" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span></a>
  
  
</li>
      <li hidden="" data-menu-item="i2pull-requests-tab" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a tabindex="-1" id="item-0ef7dd48-9c3d-48c5-8f9a-8510f2d84ded" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/pulls" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span></a>
  
  
</li>
      <li hidden="" data-menu-item="i3actions-tab" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a tabindex="-1" id="item-28036764-99e2-49ea-bbcb-2dcb1755a6c7" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/actions" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Actions
</span></a>
  
  
</li>
      <li hidden="" data-menu-item="i4projects-tab" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a tabindex="-1" id="item-3791eaf6-5369-4ad0-b0fd-ac47ccfa50da" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/projects" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span></a>
  
  
</li>
      <li hidden="" data-menu-item="i5security-tab" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a tabindex="-1" id="item-9333fbae-8b45-4e7e-978f-02bb808864dc" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/security" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Security
</span></a>
  
  
</li>
      <li hidden="" data-menu-item="i6insights-tab" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a tabindex="-1" id="item-7e91e6b5-5b60-4bc3-8ad8-1a32e03f17f3" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/pulse" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Insights
</span></a>
  
  
</li>
</ul>  
</div>

</div>
      
</div></anchored-position>  </focus-group>
</action-menu></div>
</nav>
      </div>
</header>


      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn flash-full mb-3">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a class="Link--inTextBlock" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/blob/main/AES256.py">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a class="Link--inTextBlock" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/blob/main/AES256.py">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden="">You switched accounts on another tab or window. <a class="Link--inTextBlock" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/blob/main/AES256.py">Reload</a> to refresh your session.</span>

    <button id="icon-button-1c2355e2-acde-4747-a0b3-6e5de84118b1" aria-labelledby="tooltip-11140e00-f92f-4b9b-91f6-4f6d9a8538e0" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-11140e00-f92f-4b9b-91f6-4f6d9a8538e0" for="icon-button-1c2355e2-acde-4747-a0b3-6e5de84118b1" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tool-tip-position-top, 0) auto auto var(--tool-tip-position-left, 0) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
        content: "";
        border: 6px solid transparent;
        opacity: 0;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: "";
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open),
      :host(.\:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }
      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }
      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }
      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }
      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }
      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Dismiss alert</tool-tip>


  
</div>
          
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" data-turbo-replace="">





  <template class="js-flash-template"></template>
</div>


    
    <notification-shelf-watcher data-base-url="https://github.com/notifications/beta/shelf" data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6OTcxMzE0NjUiLCJ0IjoxNzA3NzYxNDI5fQ==--7e25fde7943992c5e2112765c3f979ac496e3b3e93866882b3f4c0ca5bec1e67" data-view-component="true" class="js-socket-channel" data-refresh-delay="500" data-catalyst=""></notification-shelf-watcher>
  <div hidden="" data-initial="" data-target="notification-shelf-watcher.placeholder"></div>






      <details class="details-reset details-overlay details-overlay-dark js-command-palette-dialog" id="command-palette-pjax-container" data-turbo-replace="">
  <summary aria-label="Command palette trigger" tabindex="-1" role="button"></summary>
  <details-dialog class="command-palette-details-dialog d-flex flex-column flex-justify-center height-fit" aria-label="Command palette" role="dialog" aria-modal="true">
    <command-palette class="command-palette color-bg-default rounded-3 border color-shadow-small" return-to="/helmii18/encrypt-decrypt-pdf-file-with-AES256-/blob/main/AES256.py" user-id="97131465" activation-hotkey="Mod+k,Mod+Alt+k" command-mode-hotkey="Mod+Shift+K" data-action="
        command-palette-input-ready:command-palette#inputReady
        command-palette-page-stack-updated:command-palette#updateInputScope
        itemsUpdated:command-palette#itemsUpdated
        keydown:command-palette#onKeydown
        loadingStateChanged:command-palette#loadingStateChanged
        selectedItemChanged:command-palette#selectedItemChanged
        pageFetchError:command-palette#pageFetchError
      " data-catalyst="">

        <command-palette-mode data-char="#" data-scope-types="[&quot;&quot;]" data-placeholder="Search issues and pull requests" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="#" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-placeholder="Search issues, pull requests, discussions, and projects" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="!" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-placeholder="Search projects" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="@" data-scope-types="[&quot;&quot;]" data-placeholder="Search or jump to a user, organization, or repository" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="@" data-scope-types="[&quot;owner&quot;]" data-placeholder="Search or jump to a repository" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="/" data-scope-types="[&quot;repository&quot;]" data-placeholder="Search files" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="?" data-placeholder="" data-catalyst="" data-scope-types=""></command-palette-mode>
        <command-palette-mode data-char="&gt;" data-placeholder="Run a command" data-scope-types="" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="" data-scope-types="[&quot;&quot;]" data-placeholder="Search or jump to..." data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="" data-scope-types="[&quot;owner&quot;]" data-placeholder="Search or jump to..." data-catalyst=""></command-palette-mode>
      <command-palette-mode class="js-command-palette-default-mode" data-char="" data-placeholder="Search or jump to..." data-scope-types="" data-catalyst=""></command-palette-mode>

      <command-palette-input placeholder="Search or jump to..." data-action="
          command-palette-input:command-palette#onInput
          command-palette-select:command-palette#onSelect
          command-palette-descope:command-palette#onDescope
          command-palette-cleared:command-palette#onInputClear
        " data-catalyst="" class="d-flex flex-items-center flex-nowrap py-1 pl-3 pr-2 border-bottom">
        <div class="js-search-icon d-flex flex-items-center mr-2" style="height: 26px">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search color-fg-muted">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
        </div>
        <div class="js-spinner d-flex flex-items-center mr-2 color-fg-muted" hidden="">
          <svg aria-label="Loading" class="anim-rotate" viewBox="0 0 16 16" fill="none" width="16" height="16">
            <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
            <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
          </svg>
        </div>
        <command-palette-scope data-catalyst="" class="d-inline-flex">
          <div data-target="command-palette-scope.placeholder" hidden="" class="color-fg-subtle">/&nbsp;&nbsp;<span class="text-semibold color-fg-default">...</span>&nbsp;&nbsp;/&nbsp;&nbsp;</div>
              <command-palette-token data-text="helmii18" data-id="U_kgDOBlH0mw" data-type="owner" data-value="helmii18" data-targets="command-palette-scope.tokens" class="color-fg-default text-semibold" style="white-space:nowrap;line-height:20px;" id="" data-catalyst="">helmii18<span class="color-fg-subtle text-normal">&nbsp;&nbsp;/&nbsp;&nbsp;</span></command-palette-token>
              <command-palette-token data-text="encrypt-decrypt-pdf-file-with-AES256-" data-id="R_kgDOJJ8ioA" data-type="repository" data-value="encrypt-decrypt-pdf-file-with-AES256-" data-targets="command-palette-scope.tokens" class="color-fg-default text-semibold" style="white-space:nowrap;line-height:20px;" id="" data-catalyst="">encrypt-decrypt-p...<span class="color-fg-subtle text-normal">&nbsp;&nbsp;/&nbsp;&nbsp;</span></command-palette-token>
        </command-palette-scope>
        <div class="command-palette-input-group flex-1 form-control border-0 box-shadow-none" style="z-index: 0">
          <div class="command-palette-typeahead position-absolute d-flex flex-items-center Truncate">
            <span class="typeahead-segment input-mirror" data-target="command-palette-input.mirror"></span>
            <span class="Truncate-text" data-target="command-palette-input.typeaheadText"></span>
            <span class="typeahead-segment" data-target="command-palette-input.typeaheadPlaceholder"></span>
          </div>
          <input class="js-overlay-input typeahead-input d-none" disabled="" tabindex="-1" aria-label="Hidden input for typeahead">
          <input type="text" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" class="js-input typeahead-input form-control border-0 box-shadow-none input-block width-full no-focus-indicator" aria-label="Command palette input" aria-haspopup="listbox" aria-expanded="false" aria-autocomplete="list" aria-controls="command-palette-page-stack" role="combobox" data-action="
              input:command-palette-input#onInput
              keydown:command-palette-input#onKeydown
            " placeholder="Search or jump to...">
        </div>
          <div data-view-component="true" class="position-relative d-inline-block">
    <button aria-keyshortcuts="Control+Backspace" data-action="click:command-palette-input#onClear keypress:command-palette-input#onClear" data-target="command-palette-input.clearButton" id="command-palette-clear-button" hidden="hidden" type="button" data-view-component="true" class="btn-octicon command-palette-input-clear-button" aria-labelledby="tooltip-b8e5a024-75de-4efd-97d8-955ce3cabf9b">      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>    <tool-tip id="tooltip-b8e5a024-75de-4efd-97d8-955ce3cabf9b" for="command-palette-clear-button" popover="manual" data-direction="w" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tool-tip-position-top, 0) auto auto var(--tool-tip-position-left, 0) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
        content: "";
        border: 6px solid transparent;
        opacity: 0;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: "";
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open),
      :host(.\:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }
      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }
      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }
      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }
      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }
      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Clear Command Palette</tool-tip>
</div>
      </command-palette-input>

      <command-palette-page-stack data-default-scope-id="R_kgDOJJ8ioA" data-default-scope-type="Repository" data-action="command-palette-page-octicons-cached:command-palette-page-stack#cacheOcticons" data-current-mode="" data-catalyst="" data-target="command-palette.pageStack" data-current-query-text="">
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">#</kbd> to search pull requests
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">#</kbd> to search issues
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">#</kbd> to search discussions
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">!</kbd> to search projects
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;owner&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">@</kbd> to search teams
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">@</kbd> to search people and organizations
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">&gt;</kbd> to activate command mode
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Go to your accessibility settings to change your keyboard shortcuts
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="#" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type author:@me to search your content
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="#" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:pr to filter to pull requests
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="#" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:issue to filter to issues
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-mode="#" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:project to filter to projects
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="#" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:open to filter to open content
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
        <command-palette-tip class="mx-3 my-2 flash flash-error d-flex flex-items-center" data-scope-types="*" data-on-error="" data-mode="*" data-catalyst="" hidden="" data-match-mode="" data-value="*">
          <div>
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
          </div>
          <div class="px-2">
            We’ve encountered an error and some results aren't available at this time. Type a new search or try again later.
          </div>
        </command-palette-tip>
        <command-palette-tip class="h4 color-fg-default pl-3 pb-2 pt-3" data-on-empty="" data-scope-types="*" data-match-mode="[^?]|^$" data-mode="*" data-catalyst="" hidden="" data-value="*">
          No results matched your search
        </command-palette-tip>

        <div hidden="">

            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="arrow-right-color-fg-muted">
              <svg height="16" class="octicon octicon-arrow-right color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8.22 2.97a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l2.97-2.97H3.75a.75.75 0 0 1 0-1.5h7.44L8.22 4.03a.75.75 0 0 1 0-1.06Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="arrow-right-color-fg-default">
              <svg height="16" class="octicon octicon-arrow-right color-fg-default" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8.22 2.97a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l2.97-2.97H3.75a.75.75 0 0 1 0-1.5h7.44L8.22 4.03a.75.75 0 0 1 0-1.06Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="codespaces-color-fg-muted">
              <svg height="16" class="octicon octicon-codespaces color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="copy-color-fg-muted">
              <svg height="16" class="octicon octicon-copy color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="dash-color-fg-muted">
              <svg height="16" class="octicon octicon-dash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M2 7.75A.75.75 0 0 1 2.75 7h10a.75.75 0 0 1 0 1.5h-10A.75.75 0 0 1 2 7.75Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="file-color-fg-muted">
              <svg height="16" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="gear-color-fg-muted">
              <svg height="16" class="octicon octicon-gear color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="lock-color-fg-muted">
              <svg height="16" class="octicon octicon-lock color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M4 4a4 4 0 0 1 8 0v2h.25c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 12.25 15h-8.5A1.75 1.75 0 0 1 2 13.25v-5.5C2 6.784 2.784 6 3.75 6H4Zm8.25 3.5h-8.5a.25.25 0 0 0-.25.25v5.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25ZM10.5 6V4a2.5 2.5 0 1 0-5 0v2Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="moon-color-fg-muted">
              <svg height="16" class="octicon octicon-moon color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M9.598 1.591a.749.749 0 0 1 .785-.175 7.001 7.001 0 1 1-8.967 8.967.75.75 0 0 1 .961-.96 5.5 5.5 0 0 0 7.046-7.046.75.75 0 0 1 .175-.786Zm1.616 1.945a7 7 0 0 1-7.678 7.678 5.499 5.499 0 1 0 7.678-7.678Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="person-color-fg-muted">
              <svg height="16" class="octicon octicon-person color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M10.561 8.073a6.005 6.005 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07 4.5 4.5 0 0 0-8.99 0 .75.75 0 0 1-1.498-.07 6.004 6.004 0 0 1 3.431-5.142 3.999 3.999 0 1 1 5.123 0ZM10.5 5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="pencil-color-fg-muted">
              <svg height="16" class="octicon octicon-pencil color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="issue-opened-open">
              <svg height="16" class="octicon octicon-issue-opened open" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="git-pull-request-draft-color-fg-muted">
              <svg height="16" class="octicon octicon-git-pull-request-draft color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M3.25 1A2.25 2.25 0 0 1 4 5.372v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.251 2.251 0 0 1 3.25 1Zm9.5 14a2.25 2.25 0 1 1 0-4.5 2.25 2.25 0 0 1 0 4.5ZM2.5 3.25a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0ZM3.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm9.5 0a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM14 7.5a1.25 1.25 0 1 1-2.5 0 1.25 1.25 0 0 1 2.5 0Zm0-4.25a1.25 1.25 0 1 1-2.5 0 1.25 1.25 0 0 1 2.5 0Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="search-color-fg-muted">
              <svg height="16" class="octicon octicon-search color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="sun-color-fg-muted">
              <svg height="16" class="octicon octicon-sun color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 12a4 4 0 1 1 0-8 4 4 0 0 1 0 8Zm0-1.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5Zm5.657-8.157a.75.75 0 0 1 0 1.061l-1.061 1.06a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734l1.06-1.06a.75.75 0 0 1 1.06 0Zm-9.193 9.193a.75.75 0 0 1 0 1.06l-1.06 1.061a.75.75 0 1 1-1.061-1.06l1.06-1.061a.75.75 0 0 1 1.061 0ZM8 0a.75.75 0 0 1 .75.75v1.5a.75.75 0 0 1-1.5 0V.75A.75.75 0 0 1 8 0ZM3 8a.75.75 0 0 1-.75.75H.75a.75.75 0 0 1 0-1.5h1.5A.75.75 0 0 1 3 8Zm13 0a.75.75 0 0 1-.75.75h-1.5a.75.75 0 0 1 0-1.5h1.5A.75.75 0 0 1 16 8Zm-8 5a.75.75 0 0 1 .75.75v1.5a.75.75 0 0 1-1.5 0v-1.5A.75.75 0 0 1 8 13Zm3.536-1.464a.75.75 0 0 1 1.06 0l1.061 1.06a.75.75 0 0 1-1.06 1.061l-1.061-1.06a.75.75 0 0 1 0-1.061ZM2.343 2.343a.75.75 0 0 1 1.061 0l1.06 1.061a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018l-1.06-1.06a.75.75 0 0 1 0-1.06Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="sync-color-fg-muted">
              <svg height="16" class="octicon octicon-sync color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M1.705 8.005a.75.75 0 0 1 .834.656 5.5 5.5 0 0 0 9.592 2.97l-1.204-1.204a.25.25 0 0 1 .177-.427h3.646a.25.25 0 0 1 .25.25v3.646a.25.25 0 0 1-.427.177l-1.38-1.38A7.002 7.002 0 0 1 1.05 8.84a.75.75 0 0 1 .656-.834ZM8 2.5a5.487 5.487 0 0 0-4.131 1.869l1.204 1.204A.25.25 0 0 1 4.896 6H1.25A.25.25 0 0 1 1 5.75V2.104a.25.25 0 0 1 .427-.177l1.38 1.38A7.002 7.002 0 0 1 14.95 7.16a.75.75 0 0 1-1.49.178A5.5 5.5 0 0 0 8 2.5Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="trash-color-fg-muted">
              <svg height="16" class="octicon octicon-trash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M11 1.75V3h2.25a.75.75 0 0 1 0 1.5H2.75a.75.75 0 0 1 0-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75ZM4.496 6.675l.66 6.6a.25.25 0 0 0 .249.225h5.19a.25.25 0 0 0 .249-.225l.66-6.6a.75.75 0 0 1 1.492.149l-.66 6.6A1.748 1.748 0 0 1 10.595 15h-5.19a1.75 1.75 0 0 1-1.741-1.575l-.66-6.6a.75.75 0 1 1 1.492-.15ZM6.5 1.75V3h3V1.75a.25.25 0 0 0-.25-.25h-2.5a.25.25 0 0 0-.25.25Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="key-color-fg-muted">
              <svg height="16" class="octicon octicon-key color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M10.5 0a5.499 5.499 0 1 1-1.288 10.848l-.932.932a.749.749 0 0 1-.53.22H7v.75a.749.749 0 0 1-.22.53l-.5.5a.749.749 0 0 1-.53.22H5v.75a.749.749 0 0 1-.22.53l-.5.5a.749.749 0 0 1-.53.22h-2A1.75 1.75 0 0 1 0 14.25v-2c0-.199.079-.389.22-.53l4.932-4.932A5.5 5.5 0 0 1 10.5 0Zm-4 5.5c-.001.431.069.86.205 1.269a.75.75 0 0 1-.181.768L1.5 12.56v1.69c0 .138.112.25.25.25h1.69l.06-.06v-1.19a.75.75 0 0 1 .75-.75h1.19l.06-.06v-1.19a.75.75 0 0 1 .75-.75h1.19l1.023-1.025a.75.75 0 0 1 .768-.18A4 4 0 1 0 6.5 5.5ZM11 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="comment-discussion-color-fg-muted">
              <svg height="16" class="octicon octicon-comment-discussion color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="bell-color-fg-muted">
              <svg height="16" class="octicon octicon-bell color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 16a2 2 0 0 0 1.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 0 0 8 16ZM3 5a5 5 0 0 1 10 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.519 1.519 0 0 1 13.482 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947Zm5-3.5A3.5 3.5 0 0 0 4.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01l.001.006c0 .002.002.004.004.006l.006.004.007.001h10.964l.007-.001.006-.004.004-.006.001-.007a.017.017 0 0 0-.003-.01l-1.703-2.554a1.745 1.745 0 0 1-.294-.97V5A3.5 3.5 0 0 0 8 1.5Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="bell-slash-color-fg-muted">
              <svg height="16" class="octicon octicon-bell-slash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="m4.182 4.31.016.011 10.104 7.316.013.01 1.375.996a.75.75 0 1 1-.88 1.214L13.626 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947V5.305L.31 3.357a.75.75 0 1 1 .88-1.214Zm7.373 7.19L4.5 6.391v1.556c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01c0 .005.002.009.005.012l.006.004.007.001ZM8 1.5c-.997 0-1.895.416-2.534 1.086A.75.75 0 1 1 4.38 1.55 5 5 0 0 1 13 5v2.373a.75.75 0 0 1-1.5 0V5A3.5 3.5 0 0 0 8 1.5ZM8 16a2 2 0 0 1-1.985-1.75c-.017-.137.097-.25.235-.25h3.5c.138 0 .252.113.235.25A2 2 0 0 1 8 16Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="paintbrush-color-fg-muted">
              <svg height="16" class="octicon octicon-paintbrush color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M11.134 1.535c.7-.509 1.416-.942 2.076-1.155.649-.21 1.463-.267 2.069.34.603.601.568 1.411.368 2.07-.202.668-.624 1.39-1.125 2.096-1.011 1.424-2.496 2.987-3.775 4.249-1.098 1.084-2.132 1.839-3.04 2.3a3.744 3.744 0 0 1-1.055 3.217c-.431.431-1.065.691-1.657.861-.614.177-1.294.287-1.914.357A21.151 21.151 0 0 1 .797 16H.743l.007-.75H.749L.742 16a.75.75 0 0 1-.743-.742l.743-.008-.742.007v-.054a21.25 21.25 0 0 1 .13-2.284c.067-.647.187-1.287.358-1.914.17-.591.43-1.226.86-1.657a3.746 3.746 0 0 1 3.227-1.054c.466-.893 1.225-1.907 2.314-2.982 1.271-1.255 2.833-2.75 4.245-3.777ZM1.62 13.089c-.051.464-.086.929-.104 1.395.466-.018.932-.053 1.396-.104a10.511 10.511 0 0 0 1.668-.309c.526-.151.856-.325 1.011-.48a2.25 2.25 0 1 0-3.182-3.182c-.155.155-.329.485-.48 1.01a10.515 10.515 0 0 0-.309 1.67Zm10.396-10.34c-1.224.89-2.605 2.189-3.822 3.384l1.718 1.718c1.21-1.205 2.51-2.597 3.387-3.833.47-.662.78-1.227.912-1.662.134-.444.032-.551.009-.575h-.001V1.78c-.014-.014-.113-.113-.548.027-.432.14-.995.462-1.655.942Zm-4.832 7.266-.001.001a9.859 9.859 0 0 0 1.63-1.142L7.155 7.216a9.7 9.7 0 0 0-1.161 1.607c.482.302.889.71 1.19 1.192Z"></path></svg>
            </div>

            <command-palette-item-group data-group-id="top" data-group-title="Top result" data-group-hint="" data-group-limits="{}" data-default-priority="0" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Top result
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Top result results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="commands" data-group-title="Commands" data-group-hint="Type &gt; to filter" data-group-limits="{&quot;static_items_page&quot;:50,&quot;issue&quot;:50,&quot;pull_request&quot;:50,&quot;discussion&quot;:50}" data-default-priority="1" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Commands
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              Type &gt; to filter
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Commands results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="global_commands" data-group-title="Global Commands" data-group-hint="Type &gt; to filter" data-group-limits="{&quot;issue&quot;:0,&quot;pull_request&quot;:0,&quot;discussion&quot;:0}" data-default-priority="2" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Global Commands
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              Type &gt; to filter
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Global Commands results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="this_page" data-group-title="This Page" data-group-hint="" data-group-limits="{}" data-default-priority="3" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              This Page
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="This Page results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="files" data-group-title="Files" data-group-hint="" data-group-limits="{}" data-default-priority="4" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Files
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Files results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="default" data-group-title="Default" data-group-hint="" data-group-limits="{&quot;static_items_page&quot;:50}" data-default-priority="5" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Default results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="pages" data-group-title="Pages" data-group-hint="" data-group-limits="{&quot;repository&quot;:10}" data-default-priority="6" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Pages
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Pages results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="access_policies" data-group-title="Access Policies" data-group-hint="" data-group-limits="{}" data-default-priority="7" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Access Policies
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Access Policies results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="organizations" data-group-title="Organizations" data-group-hint="" data-group-limits="{}" data-default-priority="8" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Organizations
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Organizations results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="repositories" data-group-title="Repositories" data-group-hint="" data-group-limits="{}" data-default-priority="9" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Repositories
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Repositories results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="references" data-group-title="Issues, pull requests, and discussions" data-group-hint="Type # to filter" data-group-limits="{}" data-default-priority="10" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Issues, pull requests, and discussions
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              Type # to filter
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Issues, pull requests, and discussions results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="teams" data-group-title="Teams" data-group-hint="" data-group-limits="{}" data-default-priority="11" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Teams
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Teams results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="users" data-group-title="Users" data-group-hint="" data-group-limits="{}" data-default-priority="12" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Users
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Users results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="memex_projects" data-group-title="Projects" data-group-hint="" data-group-limits="{}" data-default-priority="13" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Projects
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Projects results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="projects" data-group-title="Projects (classic)" data-group-hint="" data-group-limits="{}" data-default-priority="14" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Projects (classic)
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Projects (classic) results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="footer" data-group-title="Footer" data-group-hint="" data-group-limits="{}" data-default-priority="15" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Footer results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="modes_help" data-group-title="Modes" data-group-hint="" data-group-limits="{}" data-default-priority="16" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Modes
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Modes results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="filters_help" data-group-title="Use filters in issues, pull requests, discussions, and projects" data-group-hint="" data-group-limits="{}" data-default-priority="17" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Use filters in issues, pull requests, discussions, and projects
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Use filters in issues, pull requests, discussions, and projects results"></div>
        </command-palette-item-group>

            <command-palette-page data-page-title="helmii18" data-scope-id="U_kgDOBlH0mw" data-scope-type="owner" data-targets="command-palette-page-stack.defaultPages" hidden="" data-catalyst="" class="rounded-bottom-2 page-stack-transition-height" style="max-height:400px;">
            </command-palette-page>
            <command-palette-page data-page-title="encrypt-decrypt-pdf-file-with-AES256-" data-scope-id="R_kgDOJJ8ioA" data-scope-type="repository" data-targets="command-palette-page-stack.defaultPages" hidden="" data-catalyst="" class="rounded-bottom-2 page-stack-transition-height" style="max-height:400px;">
            </command-palette-page>
        </div>

        <command-palette-page data-is-root="" hidden="" data-page-title="" data-catalyst="" class="rounded-bottom-2 page-stack-transition-height" data-targets="command-palette-page-stack.pages" style="max-height:400px;" data-scope-id="" data-scope-type="">
        </command-palette-page>
          <command-palette-page data-page-title="helmii18" data-scope-id="U_kgDOBlH0mw" data-scope-type="owner" hidden="" data-catalyst="" class="rounded-bottom-2 page-stack-transition-height" data-targets="command-palette-page-stack.pages" style="max-height:400px;">
          </command-palette-page>
          <command-palette-page data-page-title="encrypt-decrypt-pdf-file-with-AES256-" data-scope-id="R_kgDOJJ8ioA" data-scope-type="repository" hidden="" data-catalyst="" class="rounded-bottom-2 page-stack-transition-height" data-targets="command-palette-page-stack.pages" style="max-height:400px;">
          </command-palette-page>
      </command-palette-page-stack>

      <server-defined-provider data-type="search-links" data-targets="command-palette.serverDefinedProviderElements" data-supported-modes="" data-catalyst="" data-fetch-debounce="" data-supported-scope-types="" data-src="" data-supports-commands=""></server-defined-provider>
      <server-defined-provider data-type="help" data-targets="command-palette.serverDefinedProviderElements" data-supported-modes="" data-catalyst="" data-fetch-debounce="" data-supported-scope-types="" data-src="" data-supports-commands="">
          <command-palette-help data-group="modes_help" data-prefix="#" data-scope-types="[&quot;&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search for <strong>issues</strong> and <strong>pull requests</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">#</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="modes_help" data-prefix="#" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search for <strong>issues, pull requests, discussions,</strong> and <strong>projects</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">#</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="modes_help" data-prefix="@" data-scope-types="[&quot;&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search for <strong>organizations, repositories,</strong> and <strong>users</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">@</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="modes_help" data-prefix="!" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search for <strong>projects</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">!</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="modes_help" data-prefix="/" data-scope-types="[&quot;repository&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search for <strong>files</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">/</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="modes_help" data-prefix="&gt;" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Activate <strong>command mode</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">&gt;</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# author:@me" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search your issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># author:@me</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# author:@me" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search your issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># author:@me</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# is:pr" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Filter to pull requests</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:pr</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# is:issue" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Filter to issues</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:issue</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# is:discussion" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Filter to discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:discussion</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# is:project" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Filter to projects</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:project</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# is:open" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Filter to open issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:open</kbd>
              </span>
          </command-palette-help>
      </server-defined-provider>

        <server-defined-provider data-type="commands" data-fetch-debounce="0" data-src="/command_palette/commands" data-supported-modes="[]" data-supports-commands="" data-targets="command-palette.serverDefinedProviderElements" data-supported-scope-types="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="prefetched" data-fetch-debounce="0" data-src="/command_palette/jump_to_page_navigation" data-supported-modes="[&quot;&quot;]" data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/issues" data-supported-modes="[&quot;#&quot;,&quot;#&quot;]" data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;,&quot;&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/jump_to" data-supported-modes="[&quot;@&quot;,&quot;@&quot;]" data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/jump_to_members_only" data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;,&quot;&quot;]" data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="prefetched" data-fetch-debounce="0" data-src="/command_palette/jump_to_members_only_prefetched" data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;,&quot;&quot;]" data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="files" data-fetch-debounce="0" data-src="/command_palette/files" data-supported-modes="[&quot;/&quot;]" data-supported-scope-types="[&quot;repository&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/discussions" data-supported-modes="[&quot;#&quot;]" data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/projects" data-supported-modes="[&quot;#&quot;,&quot;!&quot;]" data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="prefetched" data-fetch-debounce="0" data-src="/command_palette/recent_issues" data-supported-modes="[&quot;#&quot;,&quot;#&quot;]" data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;,&quot;&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/teams" data-supported-modes="[&quot;@&quot;,&quot;&quot;]" data-supported-scope-types="[&quot;owner&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/name_with_owner_repository" data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;,&quot;&quot;]" data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
    <client-defined-provider data-catalyst="" data-provider-id="main-window-commands-provider" data-targets="command-palette.clientDefinedProviderElements"></client-defined-provider></command-palette>
  </details-dialog>
</details>

<div class="position-fixed bottom-0 left-0 ml-5 mb-5 js-command-palette-toasts" style="z-index: 1000">
  <div hidden="" class="Toast Toast--loading">
    <span class="Toast-icon">
      <svg class="Toast--spinner" viewBox="0 0 32 32" width="18" height="18" aria-hidden="true">
        <path fill="#959da5" d="M16 0 A16 16 0 0 0 16 32 A16 16 0 0 0 16 0 M16 4 A12 12 0 0 1 16 28 A12 12 0 0 1 16 4"></path>
        <path fill="#ffffff" d="M16 0 A16 16 0 0 1 32 16 L28 16 A12 12 0 0 0 16 4z"></path>
      </svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden="" class="anim-fade-in fast Toast Toast--error">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden="" class="anim-fade-in fast Toast Toast--warning">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>


  <div hidden="" class="anim-fade-in fast Toast Toast--success">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden="" class="anim-fade-in fast Toast">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-info">
    <path d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8Zm8-6.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13ZM6.5 7.75A.75.75 0 0 1 7.25 7h1a.75.75 0 0 1 .75.75v2.75h.25a.75.75 0 0 1 0 1.5h-2a.75.75 0 0 1 0-1.5h.25v-2h-.25a.75.75 0 0 1-.75-.75ZM8 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>
</div>


  <div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="">
        <div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container">
      
      






    
  <div id="repository-container-header" data-turbo-replace="" hidden=""></div>




<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
    <div id="repo-content-pjax-container" class="repository-content ">
      <a href="https://github.dev/" class="d-none js-github-dev-shortcut" data-hotkey=".,Mod+Alt+.">Open in github.dev</a>
  <a href="https://github.dev/" class="d-none js-github-dev-new-tab-shortcut" data-hotkey="Shift+.,Shift+&gt;,&gt;" target="_blank" rel="noopener noreferrer">Open in a new github.dev tab</a>
    <a class="d-none" data-hotkey=",,Mod+Alt+," target="_blank" href="https://github.com/codespaces/new/helmii18/encrypt-decrypt-pdf-file-with-AES256-/tree/main?resume=1">Open in codespace</a>



    
      
    





<react-app app-name="react-code-view" initial-path="/helmii18/encrypt-decrypt-pdf-file-with-AES256-/blob/main/AES256.py" style="min-height: calc(100vh - 64px)" data-ssr="true" data-lazy="false" data-alternate="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-app.embeddedData">{"payload":{"allShortcutsEnabled":true,"fileTree":{"":{"items":[{"name":"AES256.py","path":"AES256.py","contentType":"file"}],"totalCount":1}},"fileTreeProcessingTime":5.069167,"foldersToFetch":[],"repo":{"id":614408864,"defaultBranch":"main","name":"encrypt-decrypt-pdf-file-with-AES256-","ownerLogin":"helmii18","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2023-03-15T16:25:58.000+02:00","ownerAvatar":"https://avatars.githubusercontent.com/u/106034331?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":true,"treeExpanded":true,"refInfo":{"name":"main","listCacheKey":"v0:1678890593.001608","canEdit":true,"refType":"branch","currentOid":"c3502d22160cddfe24145dcb3bd4a1c905e20137"},"path":"AES256.py","currentUser":{"id":97131465,"login":"Mo23fathi","userEmail":"mohamedelsayedfathi400@gmail.com"},"blob":{"rawLines":["import numpy as np","from base64 import b64encode, b64decode","import datetime","import base64","","roundConstant = np.array([","    [0x01, 0x00, 0x00, 0x00],","    [0x02, 0x00, 0x00, 0x00],","    [0x04, 0x00, 0x00, 0x00],","    [0x08, 0x00, 0x00, 0x00],","    [0x10, 0x00, 0x00, 0x00],","    [0x20, 0x00, 0x00, 0x00],","    [0x40, 0x00, 0x00, 0x00],","    [0x80, 0x00, 0x00, 0x00],","    [0x1b, 0x00, 0x00, 0x00],","    [0x36, 0x00, 0x00, 0x00],","])","","roundConstant_8 = np.array([","    [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],","    [0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],","    [0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],","    [0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],","    [0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],","    [0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],","    [0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],","    [0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],","    [0x1b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],","    [0x36, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],","])","","","# Substitution Box: Encryption","s_box = np.array([","    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],","    [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],","    [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],","    [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],","    [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],","    [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],","    [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],","    [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],","    [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],","    [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],","    [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],","    [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],","    [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],","    [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],","    [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],","    [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16],","])","","","# Substitution Box: Decryption","invs_box = np.array([","    [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],","    [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],","    [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],","    [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],","    [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],","    [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],","    [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],","    [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],","    [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],","    [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],","    [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],","    [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],","    [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],","    [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],","    [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],","    [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d],","])","","","# Rijndael Galois Field: Encryption","encryptMDS = np.array([","    [0x02, 0x03, 0x01, 0x01],","    [0x01, 0x02, 0x03, 0x01],","    [0x01, 0x01, 0x02, 0x03],","    [0x03, 0x01, 0x01, 0x02],","])","","","# Rijndael Galois Field: Encryption 8*8","encryptMDS_8 = np.array([","    [0x02, 0x01, 0x03, 0x01, 0x01, 0x01, 0x01, 0x01],","    [0x01, 0x03, 0x01, 0x01, 0x01, 0x01, 0x01, 0x02],","    [0x03, 0x01, 0x01, 0x01, 0x01, 0x01, 0x02, 0x01],","    [0x01, 0x01, 0x01, 0x01, 0x01, 0x02, 0x01, 0x03],","    [0x01, 0x01, 0x01, 0x01, 0x02, 0x01, 0x03, 0x01],","    [0x01, 0x01, 0x01, 0x02, 0x01, 0x03, 0x01, 0x01],","    [0x01, 0x01, 0x02, 0x01, 0x03, 0x01, 0x01, 0x01],","    [0x01, 0x02, 0x01, 0x03, 0x01, 0x01, 0x01, 0x01],","])","","","# Rijndael Galois Field: Decryption","decryptMDS = np.array([","    [0x0e, 0x0b, 0x0d, 0x09],","    [0x09, 0x0e, 0x0b, 0x0d],","    [0x0d, 0x09, 0x0e, 0x0b],","    [0x0b, 0x0d, 0x09, 0x0e],","])","","# Rijndael Galois Field: Decryption 8*8","decryptMDS_8 = np.array([","    [0x0e, 0x01, 0x09, 0x01, 0x0d, 0x01, 0x0b, 0x01],","    [0x01, 0x09, 0x01, 0x0d, 0x01, 0x0b, 0x01, 0x0e],","    [0x09, 0x01, 0x0d, 0x01, 0x0b, 0x01, 0x0e, 0x01],","    [0x01, 0x0d, 0x01, 0x0b, 0x01, 0x0e, 0x01, 0x09],","    [0x0d, 0x01, 0x0b, 0x01, 0x0e, 0x01, 0x09, 0x01],","    [0x01, 0x0b, 0x01, 0x0e, 0x01, 0x09, 0x01, 0x0d],","    [0x0b, 0x01, 0x0e, 0x01, 0x09, 0x01, 0x0d, 0x01],","    [0x01, 0x0e, 0x01, 0x09, 0x01, 0x0d, 0x01, 0x0b],","])","","","# Look UP Table Mix Column:","mc2 = np.array([","    [0x00, 0x02, 0x04, 0x06, 0x08, 0x0a, 0x0c, 0x0e, 0x10, 0x12, 0x14, 0x16, 0x18, 0x1a, 0x1c, 0x1e],","    [0x20, 0x22, 0x24, 0x26, 0x28, 0x2a, 0x2c, 0x2e, 0x30, 0x32, 0x34, 0x36, 0x38, 0x3a, 0x3c, 0x3e],","    [0x40, 0x42, 0x44, 0x46, 0x48, 0x4a, 0x4c, 0x4e, 0x50, 0x52, 0x54, 0x56, 0x58, 0x5a, 0x5c, 0x5e],","    [0x60, 0x62, 0x64, 0x66, 0x68, 0x6a, 0x6c, 0x6e, 0x70, 0x72, 0x74, 0x76, 0x78, 0x7a, 0x7c, 0x7e],","    [0x80, 0x82, 0x84, 0x86, 0x88, 0x8a, 0x8c, 0x8e, 0x90, 0x92, 0x94, 0x96, 0x98, 0x9a, 0x9c, 0x9e],","    [0xa0, 0xa2, 0xa4, 0xa6, 0xa8, 0xaa, 0xac, 0xae, 0xb0, 0xb2, 0xb4, 0xb6, 0xb8, 0xba, 0xbc, 0xbe],","    [0xc0, 0xc2, 0xc4, 0xc6, 0xc8, 0xca, 0xcc, 0xce, 0xd0, 0xd2, 0xd4, 0xd6, 0xd8, 0xda, 0xdc, 0xde],","    [0xe0, 0xe2, 0xe4, 0xe6, 0xe8, 0xea, 0xec, 0xee, 0xf0, 0xf2, 0xf4, 0xf6, 0xf8, 0xfa, 0xfc, 0xfe],","    [0x1b, 0x19, 0x1f, 0x1d, 0x13, 0x11, 0x17, 0x15, 0x0b, 0x09, 0x0f, 0x0d, 0x03, 0x01, 0x07, 0x05],","    [0x3b, 0x39, 0x3f, 0x3d, 0x33, 0x31, 0x37, 0x35, 0x2b, 0x29, 0x2f, 0x2d, 0x23, 0x21, 0x27, 0x25],","    [0x5b, 0x59, 0x5f, 0x5d, 0x53, 0x51, 0x57, 0x55, 0x4b, 0x49, 0x4f, 0x4d, 0x43, 0x41, 0x47, 0x45],","    [0x7b, 0x79, 0x7f, 0x7d, 0x73, 0x71, 0x77, 0x75, 0x6b, 0x69, 0x6f, 0x6d, 0x63, 0x61, 0x67, 0x65],","    [0x9b, 0x99, 0x9f, 0x9d, 0x93, 0x91, 0x97, 0x95, 0x8b, 0x89, 0x8f, 0x8d, 0x83, 0x81, 0x87, 0x85],","    [0xbb, 0xb9, 0xbf, 0xbd, 0xb3, 0xb1, 0xb7, 0xb5, 0xab, 0xa9, 0xaf, 0xad, 0xa3, 0xa1, 0xa7, 0xa5],","    [0xdb, 0xd9, 0xdf, 0xdd, 0xd3, 0xd1, 0xd7, 0xd5, 0xcb, 0xc9, 0xcf, 0xcd, 0xc3, 0xc1, 0xc7, 0xc5],","    [0xfb, 0xf9, 0xff, 0xfd, 0xf3, 0xf1, 0xf7, 0xf5, 0xeb, 0xe9, 0xef, 0xed, 0xe3, 0xe1, 0xe7, 0xe5]","])","","","mc3 = np.array([","    [0x00, 0x03, 0x06, 0x05, 0x0c, 0x0f, 0x0a, 0x09, 0x18, 0x1b, 0x1e, 0x1d, 0x14, 0x17, 0x12, 0x11],","    [0x30, 0x33, 0x36, 0x35, 0x3c, 0x3f, 0x3a, 0x39, 0x28, 0x2b, 0x2e, 0x2d, 0x24, 0x27, 0x22, 0x21],","    [0x60, 0x63, 0x66, 0x65, 0x6c, 0x6f, 0x6a, 0x69, 0x78, 0x7b, 0x7e, 0x7d, 0x74, 0x77, 0x72, 0x71],","    [0x50, 0x53, 0x56, 0x55, 0x5c, 0x5f, 0x5a, 0x59, 0x48, 0x4b, 0x4e, 0x4d, 0x44, 0x47, 0x42, 0x41],","    [0xc0, 0xc3, 0xc6, 0xc5, 0xcc, 0xcf, 0xca, 0xc9, 0xd8, 0xdb, 0xde, 0xdd, 0xd4, 0xd7, 0xd2, 0xd1],","    [0xf0, 0xf3, 0xf6, 0xf5, 0xfc, 0xff, 0xfa, 0xf9, 0xe8, 0xeb, 0xee, 0xed, 0xe4, 0xe7, 0xe2, 0xe1],","    [0xa0, 0xa3, 0xa6, 0xa5, 0xac, 0xaf, 0xaa, 0xa9, 0xb8, 0xbb, 0xbe, 0xbd, 0xb4, 0xb7, 0xb2, 0xb1],","    [0x90, 0x93, 0x96, 0x95, 0x9c, 0x9f, 0x9a, 0x99, 0x88, 0x8b, 0x8e, 0x8d, 0x84, 0x87, 0x82, 0x81],","    [0x9b, 0x98, 0x9d, 0x9e, 0x97, 0x94, 0x91, 0x92, 0x83, 0x80, 0x85, 0x86, 0x8f, 0x8c, 0x89, 0x8a],","    [0xab, 0xa8, 0xad, 0xae, 0xa7, 0xa4, 0xa1, 0xa2, 0xb3, 0xb0, 0xb5, 0xb6, 0xbf, 0xbc, 0xb9, 0xba],","    [0xfb, 0xf8, 0xfd, 0xfe, 0xf7, 0xf4, 0xf1, 0xf2, 0xe3, 0xe0, 0xe5, 0xe6, 0xef, 0xec, 0xe9, 0xea],","    [0xcb, 0xc8, 0xcd, 0xce, 0xc7, 0xc4, 0xc1, 0xc2, 0xd3, 0xd0, 0xd5, 0xd6, 0xdf, 0xdc, 0xd9, 0xda],","    [0x5b, 0x58, 0x5d, 0x5e, 0x57, 0x54, 0x51, 0x52, 0x43, 0x40, 0x45, 0x46, 0x4f, 0x4c, 0x49, 0x4a],","    [0x6b, 0x68, 0x6d, 0x6e, 0x67, 0x64, 0x61, 0x62, 0x73, 0x70, 0x75, 0x76, 0x7f, 0x7c, 0x79, 0x7a],","    [0x3b, 0x38, 0x3d, 0x3e, 0x37, 0x34, 0x31, 0x32, 0x23, 0x20, 0x25, 0x26, 0x2f, 0x2c, 0x29, 0x2a],","    [0x0b, 0x08, 0x0d, 0x0e, 0x07, 0x04, 0x01, 0x02, 0x13, 0x10, 0x15, 0x16, 0x1f, 0x1c, 0x19, 0x1a]","])","","","mc9 = np.array([","    [0x00, 0x09, 0x12, 0x1b, 0x24, 0x2d, 0x36, 0x3f, 0x48, 0x41, 0x5a, 0x53, 0x6c, 0x65, 0x7e, 0x77],","    [0x90, 0x99, 0x82, 0x8b, 0xb4, 0xbd, 0xa6, 0xaf, 0xd8, 0xd1, 0xca, 0xc3, 0xfc, 0xf5, 0xee, 0xe7],","    [0x3b, 0x32, 0x29, 0x20, 0x1f, 0x16, 0x0d, 0x04, 0x73, 0x7a, 0x61, 0x68, 0x57, 0x5e, 0x45, 0x4c],","    [0xab, 0xa2, 0xb9, 0xb0, 0x8f, 0x86, 0x9d, 0x94, 0xe3, 0xea, 0xf1, 0xf8, 0xc7, 0xce, 0xd5, 0xdc],","    [0x76, 0x7f, 0x64, 0x6d, 0x52, 0x5b, 0x40, 0x49, 0x3e, 0x37, 0x2c, 0x25, 0x1a, 0x13, 0x08, 0x01],","    [0xe6, 0xef, 0xf4, 0xfd, 0xc2, 0xcb, 0xd0, 0xd9, 0xae, 0xa7, 0xbc, 0xb5, 0x8a, 0x83, 0x98, 0x91],","    [0x4d, 0x44, 0x5f, 0x56, 0x69, 0x60, 0x7b, 0x72, 0x05, 0x0c, 0x17, 0x1e, 0x21, 0x28, 0x33, 0x3a],","    [0xdd, 0xd4, 0xcf, 0xc6, 0xf9, 0xf0, 0xeb, 0xe2, 0x95, 0x9c, 0x87, 0x8e, 0xb1, 0xb8, 0xa3, 0xaa],","    [0xec, 0xe5, 0xfe, 0xf7, 0xc8, 0xc1, 0xda, 0xd3, 0xa4, 0xad, 0xb6, 0xbf, 0x80, 0x89, 0x92, 0x9b],","    [0x7c, 0x75, 0x6e, 0x67, 0x58, 0x51, 0x4a, 0x43, 0x34, 0x3d, 0x26, 0x2f, 0x10, 0x19, 0x02, 0x0b],","    [0xd7, 0xde, 0xc5, 0xcc, 0xf3, 0xfa, 0xe1, 0xe8, 0x9f, 0x96, 0x8d, 0x84, 0xbb, 0xb2, 0xa9, 0xa0],","    [0x47, 0x4e, 0x55, 0x5c, 0x63, 0x6a, 0x71, 0x78, 0x0f, 0x06, 0x1d, 0x14, 0x2b, 0x22, 0x39, 0x30],","    [0x9a, 0x93, 0x88, 0x81, 0xbe, 0xb7, 0xac, 0xa5, 0xd2, 0xdb, 0xc0, 0xc9, 0xf6, 0xff, 0xe4, 0xed],","    [0x0a, 0x03, 0x18, 0x11, 0x2e, 0x27, 0x3c, 0x35, 0x42, 0x4b, 0x50, 0x59, 0x66, 0x6f, 0x74, 0x7d],","    [0xa1, 0xa8, 0xb3, 0xba, 0x85, 0x8c, 0x97, 0x9e, 0xe9, 0xe0, 0xfb, 0xf2, 0xcd, 0xc4, 0xdf, 0xd6],","    [0x31, 0x38, 0x23, 0x2a, 0x15, 0x1c, 0x07, 0x0e, 0x79, 0x70, 0x6b, 0x62, 0x5d, 0x54, 0x4f, 0x46]","])","","# 0x0b","mc11 = np.array([","    [0x00, 0x0b, 0x16, 0x1d, 0x2c, 0x27, 0x3a, 0x31, 0x58, 0x53, 0x4e, 0x45, 0x74, 0x7f, 0x62, 0x69],","    [0xb0, 0xbb, 0xa6, 0xad, 0x9c, 0x97, 0x8a, 0x81, 0xe8, 0xe3, 0xfe, 0xf5, 0xc4, 0xcf, 0xd2, 0xd9],","    [0x7b, 0x70, 0x6d, 0x66, 0x57, 0x5c, 0x41, 0x4a, 0x23, 0x28, 0x35, 0x3e, 0x0f, 0x04, 0x19, 0x12],","    [0xcb, 0xc0, 0xdd, 0xd6, 0xe7, 0xec, 0xf1, 0xfa, 0x93, 0x98, 0x85, 0x8e, 0xbf, 0xb4, 0xa9, 0xa2],","    [0xf6, 0xfd, 0xe0, 0xeb, 0xda, 0xd1, 0xcc, 0xc7, 0xae, 0xa5, 0xb8, 0xb3, 0x82, 0x89, 0x94, 0x9f],","    [0x46, 0x4d, 0x50, 0x5b, 0x6a, 0x61, 0x7c, 0x77, 0x1e, 0x15, 0x08, 0x03, 0x32, 0x39, 0x24, 0x2f],","    [0x8d, 0x86, 0x9b, 0x90, 0xa1, 0xaa, 0xb7, 0xbc, 0xd5, 0xde, 0xc3, 0xc8, 0xf9, 0xf2, 0xef, 0xe4],","    [0x3d, 0x36, 0x2b, 0x20, 0x11, 0x1a, 0x07, 0x0c, 0x65, 0x6e, 0x73, 0x78, 0x49, 0x42, 0x5f, 0x54],","    [0xf7, 0xfc, 0xe1, 0xea, 0xdb, 0xd0, 0xcd, 0xc6, 0xaf, 0xa4, 0xb9, 0xb2, 0x83, 0x88, 0x95, 0x9e],","    [0x47, 0x4c, 0x51, 0x5a, 0x6b, 0x60, 0x7d, 0x76, 0x1f, 0x14, 0x09, 0x02, 0x33, 0x38, 0x25, 0x2e],","    [0x8c, 0x87, 0x9a, 0x91, 0xa0, 0xab, 0xb6, 0xbd, 0xd4, 0xdf, 0xc2, 0xc9, 0xf8, 0xf3, 0xee, 0xe5],","    [0x3c, 0x37, 0x2a, 0x21, 0x10, 0x1b, 0x06, 0x0d, 0x64, 0x6f, 0x72, 0x79, 0x48, 0x43, 0x5e, 0x55],","    [0x01, 0x0a, 0x17, 0x1c, 0x2d, 0x26, 0x3b, 0x30, 0x59, 0x52, 0x4f, 0x44, 0x75, 0x7e, 0x63, 0x68],","    [0xb1, 0xba, 0xa7, 0xac, 0x9d, 0x96, 0x8b, 0x80, 0xe9, 0xe2, 0xff, 0xf4, 0xc5, 0xce, 0xd3, 0xd8],","    [0x7a, 0x71, 0x6c, 0x67, 0x56, 0x5d, 0x40, 0x4b, 0x22, 0x29, 0x34, 0x3f, 0x0e, 0x05, 0x18, 0x13],","    [0xca, 0xc1, 0xdc, 0xd7, 0xe6, 0xed, 0xf0, 0xfb, 0x92, 0x99, 0x84, 0x8f, 0xbe, 0xb5, 0xa8, 0xa3]","])","","","# 0x0d","mc13 = np.array([","    [0x00, 0x0d, 0x1a, 0x17, 0x34, 0x39, 0x2e, 0x23, 0x68, 0x65, 0x72, 0x7f, 0x5c, 0x51, 0x46, 0x4b],","    [0xd0, 0xdd, 0xca, 0xc7, 0xe4, 0xe9, 0xfe, 0xf3, 0xb8, 0xb5, 0xa2, 0xaf, 0x8c, 0x81, 0x96, 0x9b],","    [0xbb, 0xb6, 0xa1, 0xac, 0x8f, 0x82, 0x95, 0x98, 0xd3, 0xde, 0xc9, 0xc4, 0xe7, 0xea, 0xfd, 0xf0],","    [0x6b, 0x66, 0x71, 0x7c, 0x5f, 0x52, 0x45, 0x48, 0x03, 0x0e, 0x19, 0x14, 0x37, 0x3a, 0x2d, 0x20],","    [0x6d, 0x60, 0x77, 0x7a, 0x59, 0x54, 0x43, 0x4e, 0x05, 0x08, 0x1f, 0x12, 0x31, 0x3c, 0x2b, 0x26],","    [0xbd, 0xb0, 0xa7, 0xaa, 0x89, 0x84, 0x93, 0x9e, 0xd5, 0xd8, 0xcf, 0xc2, 0xe1, 0xec, 0xfb, 0xf6],","    [0xd6, 0xdb, 0xcc, 0xc1, 0xe2, 0xef, 0xf8, 0xf5, 0xbe, 0xb3, 0xa4, 0xa9, 0x8a, 0x87, 0x90, 0x9d],","    [0x06, 0x0b, 0x1c, 0x11, 0x32, 0x3f, 0x28, 0x25, 0x6e, 0x63, 0x74, 0x79, 0x5a, 0x57, 0x40, 0x4d],","    [0xda, 0xd7, 0xc0, 0xcd, 0xee, 0xe3, 0xf4, 0xf9, 0xb2, 0xbf, 0xa8, 0xa5, 0x86, 0x8b, 0x9c, 0x91],","    [0x0a, 0x07, 0x10, 0x1d, 0x3e, 0x33, 0x24, 0x29, 0x62, 0x6f, 0x78, 0x75, 0x56, 0x5b, 0x4c, 0x41],","    [0x61, 0x6c, 0x7b, 0x76, 0x55, 0x58, 0x4f, 0x42, 0x09, 0x04, 0x13, 0x1e, 0x3d, 0x30, 0x27, 0x2a],","    [0xb1, 0xbc, 0xab, 0xa6, 0x85, 0x88, 0x9f, 0x92, 0xd9, 0xd4, 0xc3, 0xce, 0xed, 0xe0, 0xf7, 0xfa],","    [0xb7, 0xba, 0xad, 0xa0, 0x83, 0x8e, 0x99, 0x94, 0xdf, 0xd2, 0xc5, 0xc8, 0xeb, 0xe6, 0xf1, 0xfc],","    [0x67, 0x6a, 0x7d, 0x70, 0x53, 0x5e, 0x49, 0x44, 0x0f, 0x02, 0x15, 0x18, 0x3b, 0x36, 0x21, 0x2c],","    [0x0c, 0x01, 0x16, 0x1b, 0x38, 0x35, 0x22, 0x2f, 0x64, 0x69, 0x7e, 0x73, 0x50, 0x5d, 0x4a, 0x47],","    [0xdc, 0xd1, 0xc6, 0xcb, 0xe8, 0xe5, 0xf2, 0xff, 0xb4, 0xb9, 0xae, 0xa3, 0x80, 0x8d, 0x9a, 0x97]","])","","","# 0x0e","mc14 = np.array([","    [0x00, 0x0e, 0x1c, 0x12, 0x38, 0x36, 0x24, 0x2a, 0x70, 0x7e, 0x6c, 0x62, 0x48, 0x46, 0x54, 0x5a],","    [0xe0, 0xee, 0xfc, 0xf2, 0xd8, 0xd6, 0xc4, 0xca, 0x90, 0x9e, 0x8c, 0x82, 0xa8, 0xa6, 0xb4, 0xba],","    [0xdb, 0xd5, 0xc7, 0xc9, 0xe3, 0xed, 0xff, 0xf1, 0xab, 0xa5, 0xb7, 0xb9, 0x93, 0x9d, 0x8f, 0x81],","    [0x3b, 0x35, 0x27, 0x29, 0x03, 0x0d, 0x1f, 0x11, 0x4b, 0x45, 0x57, 0x59, 0x73, 0x7d, 0x6f, 0x61],","    [0xad, 0xa3, 0xb1, 0xbf, 0x95, 0x9b, 0x89, 0x87, 0xdd, 0xd3, 0xc1, 0xcf, 0xe5, 0xeb, 0xf9, 0xf7],","    [0x4d, 0x43, 0x51, 0x5f, 0x75, 0x7b, 0x69, 0x67, 0x3d, 0x33, 0x21, 0x2f, 0x05, 0x0b, 0x19, 0x17],","    [0x76, 0x78, 0x6a, 0x64, 0x4e, 0x40, 0x52, 0x5c, 0x06, 0x08, 0x1a, 0x14, 0x3e, 0x30, 0x22, 0x2c],","    [0x96, 0x98, 0x8a, 0x84, 0xae, 0xa0, 0xb2, 0xbc, 0xe6, 0xe8, 0xfa, 0xf4, 0xde, 0xd0, 0xc2, 0xcc],","    [0x41, 0x4f, 0x5d, 0x53, 0x79, 0x77, 0x65, 0x6b, 0x31, 0x3f, 0x2d, 0x23, 0x09, 0x07, 0x15, 0x1b],","    [0xa1, 0xaf, 0xbd, 0xb3, 0x99, 0x97, 0x85, 0x8b, 0xd1, 0xdf, 0xcd, 0xc3, 0xe9, 0xe7, 0xf5, 0xfb],","    [0x9a, 0x94, 0x86, 0x88, 0xa2, 0xac, 0xbe, 0xb0, 0xea, 0xe4, 0xf6, 0xf8, 0xd2, 0xdc, 0xce, 0xc0],","    [0x7a, 0x74, 0x66, 0x68, 0x42, 0x4c, 0x5e, 0x50, 0x0a, 0x04, 0x16, 0x18, 0x32, 0x3c, 0x2e, 0x20],","    [0xec, 0xe2, 0xf0, 0xfe, 0xd4, 0xda, 0xc8, 0xc6, 0x9c, 0x92, 0x80, 0x8e, 0xa4, 0xaa, 0xb8, 0xb6],","    [0x0c, 0x02, 0x10, 0x1e, 0x34, 0x3a, 0x28, 0x26, 0x7c, 0x72, 0x60, 0x6e, 0x44, 0x4a, 0x58, 0x56],","    [0x37, 0x39, 0x2b, 0x25, 0x0f, 0x01, 0x13, 0x1d, 0x47, 0x49, 0x5b, 0x55, 0x7f, 0x71, 0x63, 0x6d],","    [0xd7, 0xd9, 0xcb, 0xc5, 0xef, 0xe1, 0xf3, 0xfd, 0xa7, 0xa9, 0xbb, 0xb5, 0x9f, 0x91, 0x83, 0x8d]","])","","","","# Key to Matrix","def keyToHexArray(key, row=4, col=4):","    arr = []","    for i in key:","        arr.append(ord(i))","    arr = np.array(arr)","    arr = arr.reshape(row, col)  # 4*4 matrix","    return arr","","","# Apply left shift / RotWord","def arrayShift(arr, shift=-1):","    return np.roll(arr, shift)","","","# S-box on 1D Array","def arraySbox(arr):","    for i in range(0, len(arr)):","        lsb = arr[i] \u0026 0b00001111","        msb = (arr[i] \u0026 0b11110000) \u003e\u003e 4","        arr[i] = s_box[msb, lsb]","    return arr","","","# Inverse S-box on 1D Array","def arrayInvSbox(arr):","    for i in range(0, len(arr)):","        lsb = arr[i] \u0026 0b00001111","        msb = (arr[i] \u0026 0b11110000) \u003e\u003e 4","        arr[i] = invs_box[msb, lsb]","    return arr","","","# XOR Operation on [arr1, arr2] or [arr1,arr2,rcon(i)]","def xorArray(arr1, arr2, order=4, rcon=-1):","    xor_arr = []","    if (arr1.shape == arr2.shape and (rcon \u003e= -1 and rcon \u003c= 9)):","        if (rcon == -1):","            for i in range(len(arr1)):","                val = arr1[i] ^ arr2[i]","                xor_arr.append(val)","        else:","            rcon_arr = roundConstant[rcon]","            if (order == 8):","                rcon_arr = roundConstant_8[rcon]","            for i in range(len(arr1)):","                val = arr1[i] ^ arr2[i] ^ rcon_arr[i]","                xor_arr.append(val)","        xor_arr = np.array(xor_arr)","        return xor_arr","    else:","        print('Array must be same dimension numpy OR Rcon: roundconstant must be 0-10')","        print(arr1, arr2, rcon)","        return False","","","# Xor 2 2D array","def addRoundKey(arr1, arr2):","    return np.bitwise_xor(arr1, arr2)","","","# Substitution-box on 2D Array","def subBytes(arr, inverse=False):","    for i in arr:","        if (not inverse):","            arraySbox(i)","        else:","            arrayInvSbox(i)","    return arr","","","# Shift Row on 2D Array","def shiftRow(arr, left=True, order=4):","    shifted_arr = []","    for i in range(0, order):","        if (left):","            x = arrayShift(arr[:, i], -1 * i)  # Left circular shift: Encryption","        else:","            x = arrayShift(arr[:, i], i)  # Right circular shift: Decryption","        shifted_arr.append(x)","    shifted_arr = np.array(shifted_arr)  # Accurate","    return np.transpose(shifted_arr)","","","# Mix Column","def mixColumn(arr, order=4):","    arr = np.transpose(arr)","    mix_arr = np.zeros((order, order), dtype=int)","    encryptMDS_arr = encryptMDS","    if (order == 8):","        encryptMDS_arr = encryptMDS_8","    for i in range(0, order):","        for j in range(0, order):","            for k in range(0, order):","                if (encryptMDS_arr[i][k] == 1):","                    mix_arr[i][j] ^= arr[k][j]","                lsb = arr[k][j] \u0026 0b00001111","                msb = (arr[k][j] \u0026 0b11110000) \u003e\u003e 4","                if (encryptMDS_arr[i][k] == 2):","                    mix_arr[i][j] ^= mc2[msb, lsb]","                if (encryptMDS_arr[i][k] == 3):","                    mix_arr[i][j] ^= mc3[msb, lsb]","    return np.transpose(mix_arr)","","","# Inverse Mix Column","def inverseMixColumn(arr, order=4):","    decryptMDS_arr = decryptMDS","    if (order == 8):","        decryptMDS_arr = decryptMDS_8","    arr = np.transpose(arr)","    mix_arr = np.zeros((order, order), dtype=int)","    for i in range(0, order):","        for j in range(0, order):","            for k in range(0, order):","                if (decryptMDS_arr[i][k] == 1):","                    mix_arr[i][j] ^= arr[k][j]","                lsb = arr[k][j] \u0026 0b00001111","                msb = (arr[k][j] \u0026 0b11110000) \u003e\u003e 4","                if (decryptMDS_arr[i][k] == 9):","                    mix_arr[i][j] ^= mc9[msb, lsb]","                if (decryptMDS_arr[i][k] == 11):","                    mix_arr[i][j] ^= mc11[msb, lsb]","                if (decryptMDS_arr[i][k] == 13):","                    mix_arr[i][j] ^= mc13[msb, lsb]","                if (decryptMDS_arr[i][k] == 14):","                    mix_arr[i][j] ^= mc14[msb, lsb]","    return np.transpose(mix_arr)","","","# Decryption: ecrypted hex to matrix","'''","4*4: 16 box =\u003e 128 bits =\u003e 32 in hex (representation)","8*8: 64 box =\u003e 512 bits =\u003e 128 in hex (representation)","'''","","","def hexToMatrix(data, order=4):","    hexbit = order * order * 2","    if (len(data) == hexbit):","        val = [data[i:i + 2] for i in range(0, len(data), 2)]","        val = [int(x, 16) for x in val]","        arr = np.array(val)","        arr = arr.reshape(order, order)  # 4*4 matrix","        return arr","    else:","        print('length of encrypted data should be 32')","","class AES:","","    def __init__(self):","        self.ROUND = 14","        self.ROUNDKEY = []","","    # Key Scheduling","    def __keySchedule(self, KEY):","        ROW, COL = 8, 4","        EXPANSION = 7","        hexKey = keyToHexArray(KEY, ROW, COL)","        self.ROUNDKEY.append(hexKey)","        for i in range(0, EXPANSION):","            prev_arr = self.ROUNDKEY[-1]","            last_col = prev_arr[ROW - 1]","            shift_col = arrayShift(last_col)","            sbox_col = arraySbox(shift_col)","            col_1 = xorArray(prev_arr[0], sbox_col, i)","            col_2 = xorArray(col_1, prev_arr[1])","            col_3 = xorArray(col_2, prev_arr[2])","            col_4 = xorArray(col_3, prev_arr[3])","            # additional non-linear transformation after the fourth column","            col_5 = xorArray(arraySbox(np.copy(col_4)), prev_arr[4])","            col_6 = xorArray(col_5, prev_arr[5])","            col_7 = xorArray(col_6, prev_arr[6])","            col_8 = xorArray(col_7, prev_arr[7])","            new_arr = np.array([col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8])","            self.ROUNDKEY.append(new_arr)","        self.__convertRoundKey()","","    # Convert 8 4*8 Matrix to 15 4*4 Matrix","    def __convertRoundKey(self):","        self.ROUNDKEY = np.concatenate(self.ROUNDKEY)","        temp = []","        for i in range(self.ROUND + 1):","            temp.append(self.ROUNDKEY[i * 4:i * 4 + 4])","        self.ROUNDKEY = temp","","    # Encryption Process","    def __encryptProcess(self, TEXT):","        print(TEXT)","        hexData = keyToHexArray(TEXT)","        print(\"after convert to hexdata\" , hexData)","        cipher_arr = addRoundKey(hexData, self.ROUNDKEY[0])","        print(\"cipher arr \",cipher_arr)","        for i in range(1, self.ROUND + 1):","            print(\"\\nround \" ,i,\"\\n\")","            arr = cipher_arr","            print(\"cipher arr \", arr)","            arr = subBytes(arr)","            print(\"after sub bytes\",arr)","            arr = shiftRow(arr)","            print(\"after shift rows\",arr)","            if (i != self.ROUND):","                arr = mixColumn(arr)","                # print(\"after mix columns\",arr)","            arr = addRoundKey(arr, self.ROUNDKEY[i])","            cipher_arr = arr","        return cipher_arr","","    # Encryption Add Padding","    def __addPadding(self, data):","        bytes = 16","        bits_arr = []","        while (True):","            if (len(data) \u003e bytes):","                bits_arr.append(data[:bytes])","                data = data[bytes:]","            else:","                space = bytes - len(data)","                bits_arr.append(data + chr(space) * space)","                break","        return bits_arr","","    # Decryption Process","    def __decryptProcess(self, CIPHER_HEX):","        hexData = hexToMatrix(CIPHER_HEX)","        plain_arr = addRoundKey(hexData, self.ROUNDKEY[-1])","        for i in range(self.ROUND - 1, -1, -1):","            print(\"\\nround \", i, \"\\n\")","            arr = plain_arr","            print(\"plain arr \", arr)","            arr = shiftRow(arr, left=False)","            print(\"after inverse of shift rows\", arr)","            arr = subBytes(arr, inverse=True)","            print(\"after inverse of sub bytes\", arr)","            arr = addRoundKey(arr, self.ROUNDKEY[i])","            if (i != 0):","                arr = inverseMixColumn(arr)","                print(\"after inverse mix columns\", arr)","            plain_arr = arr","        return plain_arr","","    # Decryption Delete Padding","    def __delPadding(self, data):","        verify = data[-1]","        bytes = 16","        if (verify \u003e= 1 and verify \u003c= bytes - 1):","            pad = data[bytes - verify:]","            sameCount = pad.count(verify)","            if (sameCount == verify):","                return data[:bytes - verify]","            return data","        return data","","    # Encryption","    def encrypt(self, KEY, TEXT, type='hex'):","        text_arr = self.__addPadding(TEXT)","        print(\"after add padding\",text_arr)","        self.__keySchedule(KEY)","        hex_ecrypt = ''","        for i in text_arr:","            cipher_matrix = self.__encryptProcess(i)","            cipher_text = list(np.array(cipher_matrix).reshape(-1, ))","            for j in cipher_text:","                hex_ecrypt += f'{j:02x}'","        self.ROUNDKEY = []","        # conversion","        if (type == 'b64'):","            return b64encode(bytes.fromhex(hex_ecrypt)).decode()","        if (type == '0b'):","            return f'{int(hex_ecrypt, 16):0\u003eb}'","        if (type == '__all__'):","            return {","                'hex': hex_ecrypt,","                'b64': b64encode(bytes.fromhex(hex_ecrypt)).decode(),","                '0b': bin(int(hex_ecrypt, 16))[2:].zfill(len(hex_ecrypt) * 4)","            }","        return hex_ecrypt","","    # Decryption","    def decrypt(self, KEY, CIPHER, type='hex'):","        if type in ['hex', '0b', 'b64']:","            self.__keySchedule(KEY)","            data = ''","","            if (type == 'b64'):","                CIPHER = b64decode(CIPHER).hex()","                print(\"cipher in b64\",CIPHER)","            if (type == '0b'):","                CIPHER = hex(int(CIPHER, 2)).replace('0x', '')","                print(\"cipher in 0b\",CIPHER)","            if (len(CIPHER) % 32 == 0 and len(CIPHER) \u003e 0):","                examine = CIPHER","                while (len(examine) != 0):","                    plain_matrix = self.__decryptProcess(examine[:32])","                    plain_arr = list(np.array(plain_matrix).reshape(-1, ))","                    plain_arr = self.__delPadding(plain_arr)","                    for j in plain_arr:","                        data += chr(j)","                    if (len(examine) == 32):","                        examine = ''","                    else:","                        examine = examine[32:]","                self.ROUNDKEY = []","                return data","","            else:","                raise Exception(f\"Hex: {CIPHER}, should be non-empty multiple of 32bits\")","","        else:","            raise Exception(f\"type := ['hex', '0b', 'b64'] but got '{type}'\")","","","if (__name__ == '__main__'):","    aes256 = AES()","    key = 'Thats my Kung Fu1234567876543210'","    print(\"***************************************\")","    filenameencypt=input(\"enter file name to encryption \")+\".pdf\"","","    with open(filenameencypt, \"rb\") as pdf_file:","        encoded = base64.b64encode(pdf_file.read())","        encoded_string=encoded.decode('utf-8')","    stretime = datetime.datetime.now()","    c=(aes256.encrypt(key,encoded_string,'0b'))","    endetime = datetime.datetime.now()","    print(\"encryption takes \", (endetime - stretime).microseconds * 1000, \" milli seconds\")","    file_64_decodee10 = base64.b64decode(c)","    file_resultc = open('encryption file.pdf', 'wb')","    file_resultc.write(file_64_decodee10)","    print(\"encryption done with encryption file\")","","    print(\"***************************************\")","    filenamedecrypt=input(\"enter file to decryption\")+\".pdf\"","    with open(filenamedecrypt, \"rb\") as pdf_file:","        cc = base64.b64encode(pdf_file.read())","    strtimdec = datetime.datetime.now()","    m=aes256.decrypt(key,cc,'0b')","    endetimdec = datetime.datetime.now()","    print(\"encryption takes \", (endetimdec- strtimdec).microseconds * 1000, \" milli seconds\")","    file_64_decoded00 = base64.b64decode(m)","    file_result00 = open('decryption file.pdf', 'wb')","    file_result00.write(file_64_decoded00)","    print(\"***************************************\")","    print(\"decryption done with decryption file\")"],"stylingDirectives":[[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":12,"cssClass":"pl-s1"},{"start":13,"end":15,"cssClass":"pl-k"},{"start":16,"end":18,"cssClass":"pl-s1"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":11,"cssClass":"pl-s1"},{"start":12,"end":18,"cssClass":"pl-k"},{"start":19,"end":28,"cssClass":"pl-s1"},{"start":30,"end":39,"cssClass":"pl-s1"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":15,"cssClass":"pl-s1"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":13,"cssClass":"pl-s1"}],[],[{"start":0,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":18,"cssClass":"pl-s1"},{"start":19,"end":24,"cssClass":"pl-en"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"}],[],[],[{"start":0,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":20,"cssClass":"pl-s1"},{"start":21,"end":26,"cssClass":"pl-en"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[],[],[],[{"start":0,"end":30,"cssClass":"pl-c"}],[{"start":0,"end":5,"cssClass":"pl-s1"},{"start":6,"end":7,"cssClass":"pl-c1"},{"start":8,"end":10,"cssClass":"pl-s1"},{"start":11,"end":16,"cssClass":"pl-en"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[],[],[],[{"start":0,"end":30,"cssClass":"pl-c"}],[{"start":0,"end":8,"cssClass":"pl-s1"},{"start":9,"end":10,"cssClass":"pl-c1"},{"start":11,"end":13,"cssClass":"pl-s1"},{"start":14,"end":19,"cssClass":"pl-en"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[],[],[],[{"start":0,"end":35,"cssClass":"pl-c"}],[{"start":0,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":15,"cssClass":"pl-s1"},{"start":16,"end":21,"cssClass":"pl-en"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"}],[],[],[],[{"start":0,"end":39,"cssClass":"pl-c"}],[{"start":0,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":15,"end":17,"cssClass":"pl-s1"},{"start":18,"end":23,"cssClass":"pl-en"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[],[],[],[{"start":0,"end":35,"cssClass":"pl-c"}],[{"start":0,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":15,"cssClass":"pl-s1"},{"start":16,"end":21,"cssClass":"pl-en"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"}],[],[],[{"start":0,"end":39,"cssClass":"pl-c"}],[{"start":0,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":15,"end":17,"cssClass":"pl-s1"},{"start":18,"end":23,"cssClass":"pl-en"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"}],[],[],[],[{"start":0,"end":27,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-s1"},{"start":4,"end":5,"cssClass":"pl-c1"},{"start":6,"end":8,"cssClass":"pl-s1"},{"start":9,"end":14,"cssClass":"pl-en"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[],[],[],[{"start":0,"end":3,"cssClass":"pl-s1"},{"start":4,"end":5,"cssClass":"pl-c1"},{"start":6,"end":8,"cssClass":"pl-s1"},{"start":9,"end":14,"cssClass":"pl-en"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[],[],[],[{"start":0,"end":3,"cssClass":"pl-s1"},{"start":4,"end":5,"cssClass":"pl-c1"},{"start":6,"end":8,"cssClass":"pl-s1"},{"start":9,"end":14,"cssClass":"pl-en"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[],[],[{"start":0,"end":6,"cssClass":"pl-c"}],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":7,"end":9,"cssClass":"pl-s1"},{"start":10,"end":15,"cssClass":"pl-en"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[],[],[],[{"start":0,"end":6,"cssClass":"pl-c"}],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":7,"end":9,"cssClass":"pl-s1"},{"start":10,"end":15,"cssClass":"pl-en"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[],[],[],[{"start":0,"end":6,"cssClass":"pl-c"}],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":7,"end":9,"cssClass":"pl-s1"},{"start":10,"end":15,"cssClass":"pl-en"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-c1"},{"start":41,"end":45,"cssClass":"pl-c1"},{"start":47,"end":51,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-c1"},{"start":59,"end":63,"cssClass":"pl-c1"},{"start":65,"end":69,"cssClass":"pl-c1"},{"start":71,"end":75,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":83,"end":87,"cssClass":"pl-c1"},{"start":89,"end":93,"cssClass":"pl-c1"},{"start":95,"end":99,"cssClass":"pl-c1"}],[],[],[],[],[{"start":0,"end":15,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":17,"cssClass":"pl-en"},{"start":18,"end":21,"cssClass":"pl-s1"},{"start":23,"end":26,"cssClass":"pl-s1"},{"start":26,"end":27,"cssClass":"pl-c1"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":30,"end":33,"cssClass":"pl-s1"},{"start":33,"end":34,"cssClass":"pl-c1"},{"start":34,"end":35,"cssClass":"pl-c1"}],[{"start":4,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":13,"end":16,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":18,"cssClass":"pl-en"},{"start":19,"end":22,"cssClass":"pl-en"},{"start":23,"end":24,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":12,"cssClass":"pl-s1"},{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":22,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":13,"cssClass":"pl-s1"},{"start":14,"end":21,"cssClass":"pl-en"},{"start":22,"end":25,"cssClass":"pl-s1"},{"start":27,"end":30,"cssClass":"pl-s1"},{"start":33,"end":45,"cssClass":"pl-c"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":14,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":28,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":14,"cssClass":"pl-en"},{"start":15,"end":18,"cssClass":"pl-s1"},{"start":20,"end":25,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":26,"end":27,"cssClass":"pl-c1"},{"start":27,"end":28,"cssClass":"pl-c1"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":13,"cssClass":"pl-s1"},{"start":14,"end":18,"cssClass":"pl-en"},{"start":19,"end":22,"cssClass":"pl-s1"},{"start":24,"end":29,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":19,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":13,"cssClass":"pl-en"},{"start":14,"end":17,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":22,"end":25,"cssClass":"pl-en"},{"start":26,"end":29,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":33,"cssClass":"pl-c1"}],[{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":15,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":34,"cssClass":"pl-c1"},{"start":36,"end":38,"cssClass":"pl-c1"},{"start":39,"end":40,"cssClass":"pl-c1"}],[{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":17,"end":22,"cssClass":"pl-s1"},{"start":23,"end":26,"cssClass":"pl-s1"},{"start":28,"end":31,"cssClass":"pl-s1"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":14,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":27,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":16,"cssClass":"pl-en"},{"start":17,"end":20,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":22,"end":25,"cssClass":"pl-en"},{"start":26,"end":29,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":33,"cssClass":"pl-c1"}],[{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":15,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":34,"cssClass":"pl-c1"},{"start":36,"end":38,"cssClass":"pl-c1"},{"start":39,"end":40,"cssClass":"pl-c1"}],[{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":17,"end":25,"cssClass":"pl-s1"},{"start":26,"end":29,"cssClass":"pl-s1"},{"start":31,"end":34,"cssClass":"pl-s1"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":14,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":54,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":12,"cssClass":"pl-en"},{"start":13,"end":17,"cssClass":"pl-s1"},{"start":19,"end":23,"cssClass":"pl-s1"},{"start":25,"end":30,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-c1"},{"start":31,"end":32,"cssClass":"pl-c1"},{"start":34,"end":38,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-c1"},{"start":39,"end":40,"cssClass":"pl-c1"},{"start":40,"end":41,"cssClass":"pl-c1"}],[{"start":4,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":18,"cssClass":"pl-s1"},{"start":19,"end":21,"cssClass":"pl-c1"},{"start":22,"end":26,"cssClass":"pl-s1"},{"start":27,"end":32,"cssClass":"pl-s1"},{"start":33,"end":36,"cssClass":"pl-c1"},{"start":38,"end":42,"cssClass":"pl-s1"},{"start":43,"end":45,"cssClass":"pl-c1"},{"start":46,"end":47,"cssClass":"pl-c1"},{"start":47,"end":48,"cssClass":"pl-c1"},{"start":49,"end":52,"cssClass":"pl-c1"},{"start":53,"end":57,"cssClass":"pl-s1"},{"start":58,"end":60,"cssClass":"pl-c1"},{"start":61,"end":62,"cssClass":"pl-c1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":12,"end":16,"cssClass":"pl-s1"},{"start":17,"end":19,"cssClass":"pl-c1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":21,"end":22,"cssClass":"pl-c1"}],[{"start":12,"end":15,"cssClass":"pl-k"},{"start":16,"end":17,"cssClass":"pl-s1"},{"start":18,"end":20,"cssClass":"pl-c1"},{"start":21,"end":26,"cssClass":"pl-en"},{"start":27,"end":30,"cssClass":"pl-en"},{"start":31,"end":35,"cssClass":"pl-s1"}],[{"start":16,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":26,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-c1"},{"start":32,"end":36,"cssClass":"pl-s1"},{"start":37,"end":38,"cssClass":"pl-s1"}],[{"start":16,"end":23,"cssClass":"pl-s1"},{"start":24,"end":30,"cssClass":"pl-en"},{"start":31,"end":34,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-k"}],[{"start":12,"end":20,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":36,"cssClass":"pl-s1"},{"start":37,"end":41,"cssClass":"pl-s1"}],[{"start":12,"end":14,"cssClass":"pl-k"},{"start":16,"end":21,"cssClass":"pl-s1"},{"start":22,"end":24,"cssClass":"pl-c1"},{"start":25,"end":26,"cssClass":"pl-c1"}],[{"start":16,"end":24,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":27,"end":42,"cssClass":"pl-s1"},{"start":43,"end":47,"cssClass":"pl-s1"}],[{"start":12,"end":15,"cssClass":"pl-k"},{"start":16,"end":17,"cssClass":"pl-s1"},{"start":18,"end":20,"cssClass":"pl-c1"},{"start":21,"end":26,"cssClass":"pl-en"},{"start":27,"end":30,"cssClass":"pl-en"},{"start":31,"end":35,"cssClass":"pl-s1"}],[{"start":16,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":26,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-c1"},{"start":32,"end":36,"cssClass":"pl-s1"},{"start":37,"end":38,"cssClass":"pl-s1"},{"start":40,"end":41,"cssClass":"pl-c1"},{"start":42,"end":50,"cssClass":"pl-s1"},{"start":51,"end":52,"cssClass":"pl-s1"}],[{"start":16,"end":23,"cssClass":"pl-s1"},{"start":24,"end":30,"cssClass":"pl-en"},{"start":31,"end":34,"cssClass":"pl-s1"}],[{"start":8,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":20,"cssClass":"pl-s1"},{"start":21,"end":26,"cssClass":"pl-en"},{"start":27,"end":34,"cssClass":"pl-s1"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":22,"cssClass":"pl-s1"}],[{"start":4,"end":8,"cssClass":"pl-k"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":86,"cssClass":"pl-s"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":18,"cssClass":"pl-s1"},{"start":20,"end":24,"cssClass":"pl-s1"},{"start":26,"end":30,"cssClass":"pl-s1"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":20,"cssClass":"pl-c1"}],[],[],[{"start":0,"end":16,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":15,"cssClass":"pl-en"},{"start":16,"end":20,"cssClass":"pl-s1"},{"start":22,"end":26,"cssClass":"pl-s1"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":13,"cssClass":"pl-s1"},{"start":14,"end":25,"cssClass":"pl-en"},{"start":26,"end":30,"cssClass":"pl-s1"},{"start":32,"end":36,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":30,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":12,"cssClass":"pl-en"},{"start":13,"end":16,"cssClass":"pl-s1"},{"start":18,"end":25,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":26,"end":31,"cssClass":"pl-c1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":13,"end":16,"cssClass":"pl-s1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":12,"end":15,"cssClass":"pl-c1"},{"start":16,"end":23,"cssClass":"pl-s1"}],[{"start":12,"end":21,"cssClass":"pl-en"},{"start":22,"end":23,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-k"}],[{"start":12,"end":24,"cssClass":"pl-en"},{"start":25,"end":26,"cssClass":"pl-s1"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":14,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":23,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":12,"cssClass":"pl-en"},{"start":13,"end":16,"cssClass":"pl-s1"},{"start":18,"end":22,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-c1"},{"start":29,"end":34,"cssClass":"pl-s1"},{"start":34,"end":35,"cssClass":"pl-c1"},{"start":35,"end":36,"cssClass":"pl-c1"}],[{"start":4,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":22,"end":27,"cssClass":"pl-s1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":12,"end":16,"cssClass":"pl-s1"}],[{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":26,"cssClass":"pl-en"},{"start":27,"end":30,"cssClass":"pl-s1"},{"start":34,"end":35,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-c1"},{"start":39,"end":40,"cssClass":"pl-c1"},{"start":41,"end":42,"cssClass":"pl-c1"},{"start":43,"end":44,"cssClass":"pl-s1"},{"start":47,"end":80,"cssClass":"pl-c"}],[{"start":8,"end":12,"cssClass":"pl-k"}],[{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":26,"cssClass":"pl-en"},{"start":27,"end":30,"cssClass":"pl-s1"},{"start":34,"end":35,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-s1"},{"start":42,"end":76,"cssClass":"pl-c"}],[{"start":8,"end":19,"cssClass":"pl-s1"},{"start":20,"end":26,"cssClass":"pl-en"},{"start":27,"end":28,"cssClass":"pl-s1"}],[{"start":4,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":20,"cssClass":"pl-s1"},{"start":21,"end":26,"cssClass":"pl-en"},{"start":27,"end":38,"cssClass":"pl-s1"},{"start":41,"end":51,"cssClass":"pl-c"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":13,"cssClass":"pl-s1"},{"start":14,"end":23,"cssClass":"pl-en"},{"start":24,"end":35,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":12,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":13,"cssClass":"pl-en"},{"start":14,"end":17,"cssClass":"pl-s1"},{"start":19,"end":24,"cssClass":"pl-s1"},{"start":24,"end":25,"cssClass":"pl-c1"},{"start":25,"end":26,"cssClass":"pl-c1"}],[{"start":4,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":12,"cssClass":"pl-s1"},{"start":13,"end":22,"cssClass":"pl-en"},{"start":23,"end":26,"cssClass":"pl-s1"}],[{"start":4,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":16,"cssClass":"pl-s1"},{"start":17,"end":22,"cssClass":"pl-en"},{"start":24,"end":29,"cssClass":"pl-s1"},{"start":31,"end":36,"cssClass":"pl-s1"},{"start":39,"end":44,"cssClass":"pl-s1"},{"start":44,"end":45,"cssClass":"pl-c1"},{"start":45,"end":48,"cssClass":"pl-s1"}],[{"start":4,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":31,"cssClass":"pl-s1"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":8,"end":13,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-c1"},{"start":17,"end":18,"cssClass":"pl-c1"}],[{"start":8,"end":22,"cssClass":"pl-s1"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":25,"end":37,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":22,"end":27,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-k"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-c1"},{"start":17,"end":22,"cssClass":"pl-en"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":26,"end":31,"cssClass":"pl-s1"}],[{"start":12,"end":15,"cssClass":"pl-k"},{"start":16,"end":17,"cssClass":"pl-s1"},{"start":18,"end":20,"cssClass":"pl-c1"},{"start":21,"end":26,"cssClass":"pl-en"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":30,"end":35,"cssClass":"pl-s1"}],[{"start":16,"end":18,"cssClass":"pl-k"},{"start":20,"end":34,"cssClass":"pl-s1"},{"start":35,"end":36,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-s1"},{"start":41,"end":43,"cssClass":"pl-c1"},{"start":44,"end":45,"cssClass":"pl-c1"}],[{"start":20,"end":27,"cssClass":"pl-s1"},{"start":28,"end":29,"cssClass":"pl-s1"},{"start":31,"end":32,"cssClass":"pl-s1"},{"start":37,"end":40,"cssClass":"pl-s1"},{"start":41,"end":42,"cssClass":"pl-s1"},{"start":44,"end":45,"cssClass":"pl-s1"}],[{"start":16,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":25,"cssClass":"pl-s1"},{"start":26,"end":27,"cssClass":"pl-s1"},{"start":29,"end":30,"cssClass":"pl-s1"},{"start":32,"end":33,"cssClass":"pl-c1"},{"start":34,"end":44,"cssClass":"pl-c1"}],[{"start":16,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":23,"end":26,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-s1"},{"start":33,"end":34,"cssClass":"pl-c1"},{"start":35,"end":45,"cssClass":"pl-c1"},{"start":47,"end":49,"cssClass":"pl-c1"},{"start":50,"end":51,"cssClass":"pl-c1"}],[{"start":16,"end":18,"cssClass":"pl-k"},{"start":20,"end":34,"cssClass":"pl-s1"},{"start":35,"end":36,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-s1"},{"start":41,"end":43,"cssClass":"pl-c1"},{"start":44,"end":45,"cssClass":"pl-c1"}],[{"start":20,"end":27,"cssClass":"pl-s1"},{"start":28,"end":29,"cssClass":"pl-s1"},{"start":31,"end":32,"cssClass":"pl-s1"},{"start":37,"end":40,"cssClass":"pl-s1"},{"start":41,"end":44,"cssClass":"pl-s1"},{"start":46,"end":49,"cssClass":"pl-s1"}],[{"start":16,"end":18,"cssClass":"pl-k"},{"start":20,"end":34,"cssClass":"pl-s1"},{"start":35,"end":36,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-s1"},{"start":41,"end":43,"cssClass":"pl-c1"},{"start":44,"end":45,"cssClass":"pl-c1"}],[{"start":20,"end":27,"cssClass":"pl-s1"},{"start":28,"end":29,"cssClass":"pl-s1"},{"start":31,"end":32,"cssClass":"pl-s1"},{"start":37,"end":40,"cssClass":"pl-s1"},{"start":41,"end":44,"cssClass":"pl-s1"},{"start":46,"end":49,"cssClass":"pl-s1"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":13,"cssClass":"pl-s1"},{"start":14,"end":23,"cssClass":"pl-en"},{"start":24,"end":31,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":20,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":20,"cssClass":"pl-en"},{"start":21,"end":24,"cssClass":"pl-s1"},{"start":26,"end":31,"cssClass":"pl-s1"},{"start":31,"end":32,"cssClass":"pl-c1"},{"start":32,"end":33,"cssClass":"pl-c1"}],[{"start":4,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":31,"cssClass":"pl-s1"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":8,"end":13,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-c1"},{"start":17,"end":18,"cssClass":"pl-c1"}],[{"start":8,"end":22,"cssClass":"pl-s1"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":25,"end":37,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":12,"cssClass":"pl-s1"},{"start":13,"end":22,"cssClass":"pl-en"},{"start":23,"end":26,"cssClass":"pl-s1"}],[{"start":4,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":16,"cssClass":"pl-s1"},{"start":17,"end":22,"cssClass":"pl-en"},{"start":24,"end":29,"cssClass":"pl-s1"},{"start":31,"end":36,"cssClass":"pl-s1"},{"start":39,"end":44,"cssClass":"pl-s1"},{"start":44,"end":45,"cssClass":"pl-c1"},{"start":45,"end":48,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":22,"end":27,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-k"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-c1"},{"start":17,"end":22,"cssClass":"pl-en"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":26,"end":31,"cssClass":"pl-s1"}],[{"start":12,"end":15,"cssClass":"pl-k"},{"start":16,"end":17,"cssClass":"pl-s1"},{"start":18,"end":20,"cssClass":"pl-c1"},{"start":21,"end":26,"cssClass":"pl-en"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":30,"end":35,"cssClass":"pl-s1"}],[{"start":16,"end":18,"cssClass":"pl-k"},{"start":20,"end":34,"cssClass":"pl-s1"},{"start":35,"end":36,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-s1"},{"start":41,"end":43,"cssClass":"pl-c1"},{"start":44,"end":45,"cssClass":"pl-c1"}],[{"start":20,"end":27,"cssClass":"pl-s1"},{"start":28,"end":29,"cssClass":"pl-s1"},{"start":31,"end":32,"cssClass":"pl-s1"},{"start":37,"end":40,"cssClass":"pl-s1"},{"start":41,"end":42,"cssClass":"pl-s1"},{"start":44,"end":45,"cssClass":"pl-s1"}],[{"start":16,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":25,"cssClass":"pl-s1"},{"start":26,"end":27,"cssClass":"pl-s1"},{"start":29,"end":30,"cssClass":"pl-s1"},{"start":32,"end":33,"cssClass":"pl-c1"},{"start":34,"end":44,"cssClass":"pl-c1"}],[{"start":16,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":23,"end":26,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-s1"},{"start":33,"end":34,"cssClass":"pl-c1"},{"start":35,"end":45,"cssClass":"pl-c1"},{"start":47,"end":49,"cssClass":"pl-c1"},{"start":50,"end":51,"cssClass":"pl-c1"}],[{"start":16,"end":18,"cssClass":"pl-k"},{"start":20,"end":34,"cssClass":"pl-s1"},{"start":35,"end":36,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-s1"},{"start":41,"end":43,"cssClass":"pl-c1"},{"start":44,"end":45,"cssClass":"pl-c1"}],[{"start":20,"end":27,"cssClass":"pl-s1"},{"start":28,"end":29,"cssClass":"pl-s1"},{"start":31,"end":32,"cssClass":"pl-s1"},{"start":37,"end":40,"cssClass":"pl-s1"},{"start":41,"end":44,"cssClass":"pl-s1"},{"start":46,"end":49,"cssClass":"pl-s1"}],[{"start":16,"end":18,"cssClass":"pl-k"},{"start":20,"end":34,"cssClass":"pl-s1"},{"start":35,"end":36,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-s1"},{"start":41,"end":43,"cssClass":"pl-c1"},{"start":44,"end":46,"cssClass":"pl-c1"}],[{"start":20,"end":27,"cssClass":"pl-s1"},{"start":28,"end":29,"cssClass":"pl-s1"},{"start":31,"end":32,"cssClass":"pl-s1"},{"start":37,"end":41,"cssClass":"pl-s1"},{"start":42,"end":45,"cssClass":"pl-s1"},{"start":47,"end":50,"cssClass":"pl-s1"}],[{"start":16,"end":18,"cssClass":"pl-k"},{"start":20,"end":34,"cssClass":"pl-s1"},{"start":35,"end":36,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-s1"},{"start":41,"end":43,"cssClass":"pl-c1"},{"start":44,"end":46,"cssClass":"pl-c1"}],[{"start":20,"end":27,"cssClass":"pl-s1"},{"start":28,"end":29,"cssClass":"pl-s1"},{"start":31,"end":32,"cssClass":"pl-s1"},{"start":37,"end":41,"cssClass":"pl-s1"},{"start":42,"end":45,"cssClass":"pl-s1"},{"start":47,"end":50,"cssClass":"pl-s1"}],[{"start":16,"end":18,"cssClass":"pl-k"},{"start":20,"end":34,"cssClass":"pl-s1"},{"start":35,"end":36,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-s1"},{"start":41,"end":43,"cssClass":"pl-c1"},{"start":44,"end":46,"cssClass":"pl-c1"}],[{"start":20,"end":27,"cssClass":"pl-s1"},{"start":28,"end":29,"cssClass":"pl-s1"},{"start":31,"end":32,"cssClass":"pl-s1"},{"start":37,"end":41,"cssClass":"pl-s1"},{"start":42,"end":45,"cssClass":"pl-s1"},{"start":47,"end":50,"cssClass":"pl-s1"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":13,"cssClass":"pl-s1"},{"start":14,"end":23,"cssClass":"pl-en"},{"start":24,"end":31,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":36,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-s"}],[{"start":0,"end":53,"cssClass":"pl-s"}],[{"start":0,"end":54,"cssClass":"pl-s"}],[{"start":0,"end":3,"cssClass":"pl-s"}],[],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":15,"cssClass":"pl-en"},{"start":16,"end":20,"cssClass":"pl-s1"},{"start":22,"end":27,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":28,"end":29,"cssClass":"pl-c1"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":26,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":29,"end":30,"cssClass":"pl-c1"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":8,"end":11,"cssClass":"pl-en"},{"start":12,"end":16,"cssClass":"pl-s1"},{"start":18,"end":20,"cssClass":"pl-c1"},{"start":21,"end":27,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-s1"},{"start":24,"end":25,"cssClass":"pl-c1"},{"start":26,"end":27,"cssClass":"pl-c1"},{"start":29,"end":32,"cssClass":"pl-k"},{"start":33,"end":34,"cssClass":"pl-s1"},{"start":35,"end":37,"cssClass":"pl-c1"},{"start":38,"end":43,"cssClass":"pl-en"},{"start":44,"end":45,"cssClass":"pl-c1"},{"start":47,"end":50,"cssClass":"pl-en"},{"start":51,"end":55,"cssClass":"pl-s1"},{"start":58,"end":59,"cssClass":"pl-c1"}],[{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":15,"end":18,"cssClass":"pl-en"},{"start":19,"end":20,"cssClass":"pl-s1"},{"start":22,"end":24,"cssClass":"pl-c1"},{"start":26,"end":29,"cssClass":"pl-k"},{"start":30,"end":31,"cssClass":"pl-s1"},{"start":32,"end":34,"cssClass":"pl-c1"},{"start":35,"end":38,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":16,"cssClass":"pl-s1"},{"start":17,"end":22,"cssClass":"pl-en"},{"start":23,"end":26,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":17,"cssClass":"pl-s1"},{"start":18,"end":25,"cssClass":"pl-en"},{"start":26,"end":31,"cssClass":"pl-s1"},{"start":33,"end":38,"cssClass":"pl-s1"},{"start":41,"end":53,"cssClass":"pl-c"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":18,"cssClass":"pl-s1"}],[{"start":4,"end":8,"cssClass":"pl-k"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":53,"cssClass":"pl-s"}],[],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":9,"cssClass":"pl-v"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":16,"cssClass":"pl-en"},{"start":17,"end":21,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":18,"cssClass":"pl-v"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":23,"cssClass":"pl-c1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":21,"cssClass":"pl-v"},{"start":22,"end":23,"cssClass":"pl-c1"}],[],[{"start":4,"end":20,"cssClass":"pl-c"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":21,"cssClass":"pl-en"},{"start":22,"end":26,"cssClass":"pl-s1"},{"start":28,"end":31,"cssClass":"pl-v"}],[{"start":8,"end":11,"cssClass":"pl-v"},{"start":13,"end":16,"cssClass":"pl-v"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":22,"end":23,"cssClass":"pl-c1"}],[{"start":8,"end":17,"cssClass":"pl-v"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":21,"cssClass":"pl-c1"}],[{"start":8,"end":14,"cssClass":"pl-s1"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":17,"end":30,"cssClass":"pl-en"},{"start":31,"end":34,"cssClass":"pl-v"},{"start":36,"end":39,"cssClass":"pl-v"},{"start":41,"end":44,"cssClass":"pl-v"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":21,"cssClass":"pl-v"},{"start":22,"end":28,"cssClass":"pl-en"},{"start":29,"end":35,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-k"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-c1"},{"start":17,"end":22,"cssClass":"pl-en"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":26,"end":35,"cssClass":"pl-v"}],[{"start":12,"end":20,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-s1"},{"start":28,"end":36,"cssClass":"pl-v"},{"start":37,"end":38,"cssClass":"pl-c1"},{"start":38,"end":39,"cssClass":"pl-c1"}],[{"start":12,"end":20,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":31,"cssClass":"pl-s1"},{"start":32,"end":35,"cssClass":"pl-v"},{"start":36,"end":37,"cssClass":"pl-c1"},{"start":38,"end":39,"cssClass":"pl-c1"}],[{"start":12,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":34,"cssClass":"pl-en"},{"start":35,"end":43,"cssClass":"pl-s1"}],[{"start":12,"end":20,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":32,"cssClass":"pl-en"},{"start":33,"end":42,"cssClass":"pl-s1"}],[{"start":12,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":28,"cssClass":"pl-en"},{"start":29,"end":37,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-c1"},{"start":42,"end":50,"cssClass":"pl-s1"},{"start":52,"end":53,"cssClass":"pl-s1"}],[{"start":12,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":28,"cssClass":"pl-en"},{"start":29,"end":34,"cssClass":"pl-s1"},{"start":36,"end":44,"cssClass":"pl-s1"},{"start":45,"end":46,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":28,"cssClass":"pl-en"},{"start":29,"end":34,"cssClass":"pl-s1"},{"start":36,"end":44,"cssClass":"pl-s1"},{"start":45,"end":46,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":28,"cssClass":"pl-en"},{"start":29,"end":34,"cssClass":"pl-s1"},{"start":36,"end":44,"cssClass":"pl-s1"},{"start":45,"end":46,"cssClass":"pl-c1"}],[{"start":12,"end":74,"cssClass":"pl-c"}],[{"start":12,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":28,"cssClass":"pl-en"},{"start":29,"end":38,"cssClass":"pl-en"},{"start":39,"end":41,"cssClass":"pl-s1"},{"start":42,"end":46,"cssClass":"pl-en"},{"start":47,"end":52,"cssClass":"pl-s1"},{"start":56,"end":64,"cssClass":"pl-s1"},{"start":65,"end":66,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":28,"cssClass":"pl-en"},{"start":29,"end":34,"cssClass":"pl-s1"},{"start":36,"end":44,"cssClass":"pl-s1"},{"start":45,"end":46,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":28,"cssClass":"pl-en"},{"start":29,"end":34,"cssClass":"pl-s1"},{"start":36,"end":44,"cssClass":"pl-s1"},{"start":45,"end":46,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":28,"cssClass":"pl-en"},{"start":29,"end":34,"cssClass":"pl-s1"},{"start":36,"end":44,"cssClass":"pl-s1"},{"start":45,"end":46,"cssClass":"pl-c1"}],[{"start":12,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":24,"cssClass":"pl-s1"},{"start":25,"end":30,"cssClass":"pl-en"},{"start":32,"end":37,"cssClass":"pl-s1"},{"start":39,"end":44,"cssClass":"pl-s1"},{"start":46,"end":51,"cssClass":"pl-s1"},{"start":53,"end":58,"cssClass":"pl-s1"},{"start":60,"end":65,"cssClass":"pl-s1"},{"start":67,"end":72,"cssClass":"pl-s1"},{"start":74,"end":79,"cssClass":"pl-s1"},{"start":81,"end":86,"cssClass":"pl-s1"}],[{"start":12,"end":16,"cssClass":"pl-s1"},{"start":17,"end":25,"cssClass":"pl-v"},{"start":26,"end":32,"cssClass":"pl-en"},{"start":33,"end":40,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":30,"cssClass":"pl-en"}],[],[{"start":4,"end":43,"cssClass":"pl-c"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":25,"cssClass":"pl-en"},{"start":26,"end":30,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":21,"cssClass":"pl-v"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":26,"cssClass":"pl-s1"},{"start":27,"end":38,"cssClass":"pl-en"},{"start":39,"end":43,"cssClass":"pl-s1"},{"start":44,"end":52,"cssClass":"pl-v"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"}],[{"start":8,"end":11,"cssClass":"pl-k"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-c1"},{"start":17,"end":22,"cssClass":"pl-en"},{"start":23,"end":27,"cssClass":"pl-s1"},{"start":28,"end":33,"cssClass":"pl-v"},{"start":34,"end":35,"cssClass":"pl-c1"},{"start":36,"end":37,"cssClass":"pl-c1"}],[{"start":12,"end":16,"cssClass":"pl-s1"},{"start":17,"end":23,"cssClass":"pl-en"},{"start":24,"end":28,"cssClass":"pl-s1"},{"start":29,"end":37,"cssClass":"pl-v"},{"start":38,"end":39,"cssClass":"pl-s1"},{"start":40,"end":41,"cssClass":"pl-c1"},{"start":42,"end":43,"cssClass":"pl-c1"},{"start":44,"end":45,"cssClass":"pl-s1"},{"start":46,"end":47,"cssClass":"pl-c1"},{"start":48,"end":49,"cssClass":"pl-c1"},{"start":50,"end":51,"cssClass":"pl-c1"},{"start":52,"end":53,"cssClass":"pl-c1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":21,"cssClass":"pl-v"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":28,"cssClass":"pl-s1"}],[],[{"start":4,"end":24,"cssClass":"pl-c"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":24,"cssClass":"pl-en"},{"start":25,"end":29,"cssClass":"pl-s1"},{"start":31,"end":35,"cssClass":"pl-v"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":18,"cssClass":"pl-v"}],[{"start":8,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":31,"cssClass":"pl-en"},{"start":32,"end":36,"cssClass":"pl-v"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":40,"cssClass":"pl-s"},{"start":43,"end":50,"cssClass":"pl-s1"}],[{"start":8,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":32,"cssClass":"pl-en"},{"start":33,"end":40,"cssClass":"pl-s1"},{"start":42,"end":46,"cssClass":"pl-s1"},{"start":47,"end":55,"cssClass":"pl-v"},{"start":56,"end":57,"cssClass":"pl-c1"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":27,"cssClass":"pl-s"},{"start":28,"end":38,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-k"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-c1"},{"start":17,"end":22,"cssClass":"pl-en"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":26,"end":30,"cssClass":"pl-s1"},{"start":31,"end":36,"cssClass":"pl-v"},{"start":37,"end":38,"cssClass":"pl-c1"},{"start":39,"end":40,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":28,"cssClass":"pl-s"},{"start":19,"end":21,"cssClass":"pl-cce"},{"start":30,"end":31,"cssClass":"pl-s1"},{"start":32,"end":36,"cssClass":"pl-s"},{"start":33,"end":35,"cssClass":"pl-cce"}],[{"start":12,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":28,"cssClass":"pl-s1"}],[{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":31,"cssClass":"pl-s"},{"start":33,"end":36,"cssClass":"pl-s1"}],[{"start":12,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":26,"cssClass":"pl-en"},{"start":27,"end":30,"cssClass":"pl-s1"}],[{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":35,"cssClass":"pl-s"},{"start":36,"end":39,"cssClass":"pl-s1"}],[{"start":12,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":26,"cssClass":"pl-en"},{"start":27,"end":30,"cssClass":"pl-s1"}],[{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":36,"cssClass":"pl-s"},{"start":37,"end":40,"cssClass":"pl-s1"}],[{"start":12,"end":14,"cssClass":"pl-k"},{"start":16,"end":17,"cssClass":"pl-s1"},{"start":18,"end":20,"cssClass":"pl-c1"},{"start":21,"end":25,"cssClass":"pl-s1"},{"start":26,"end":31,"cssClass":"pl-v"}],[{"start":16,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":31,"cssClass":"pl-en"},{"start":32,"end":35,"cssClass":"pl-s1"}],[{"start":16,"end":48,"cssClass":"pl-c"}],[{"start":12,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":29,"cssClass":"pl-en"},{"start":30,"end":33,"cssClass":"pl-s1"},{"start":35,"end":39,"cssClass":"pl-s1"},{"start":40,"end":48,"cssClass":"pl-v"},{"start":49,"end":50,"cssClass":"pl-s1"}],[{"start":12,"end":22,"cssClass":"pl-s1"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":25,"end":28,"cssClass":"pl-s1"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":25,"cssClass":"pl-s1"}],[],[{"start":4,"end":28,"cssClass":"pl-c"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":20,"cssClass":"pl-en"},{"start":21,"end":25,"cssClass":"pl-s1"},{"start":27,"end":31,"cssClass":"pl-s1"}],[{"start":8,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":18,"cssClass":"pl-c1"}],[{"start":8,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"}],[{"start":8,"end":13,"cssClass":"pl-k"},{"start":15,"end":19,"cssClass":"pl-c1"}],[{"start":12,"end":14,"cssClass":"pl-k"},{"start":16,"end":19,"cssClass":"pl-en"},{"start":20,"end":24,"cssClass":"pl-s1"},{"start":26,"end":27,"cssClass":"pl-c1"},{"start":28,"end":33,"cssClass":"pl-s1"}],[{"start":16,"end":24,"cssClass":"pl-s1"},{"start":25,"end":31,"cssClass":"pl-en"},{"start":32,"end":36,"cssClass":"pl-s1"},{"start":38,"end":43,"cssClass":"pl-s1"}],[{"start":16,"end":20,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-s1"},{"start":28,"end":33,"cssClass":"pl-s1"}],[{"start":12,"end":16,"cssClass":"pl-k"}],[{"start":16,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":29,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-c1"},{"start":32,"end":35,"cssClass":"pl-en"},{"start":36,"end":40,"cssClass":"pl-s1"}],[{"start":16,"end":24,"cssClass":"pl-s1"},{"start":25,"end":31,"cssClass":"pl-en"},{"start":32,"end":36,"cssClass":"pl-s1"},{"start":37,"end":38,"cssClass":"pl-c1"},{"start":39,"end":42,"cssClass":"pl-en"},{"start":43,"end":48,"cssClass":"pl-s1"},{"start":50,"end":51,"cssClass":"pl-c1"},{"start":52,"end":57,"cssClass":"pl-s1"}],[{"start":16,"end":21,"cssClass":"pl-k"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":23,"cssClass":"pl-s1"}],[],[{"start":4,"end":24,"cssClass":"pl-c"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":24,"cssClass":"pl-en"},{"start":25,"end":29,"cssClass":"pl-s1"},{"start":31,"end":41,"cssClass":"pl-v"}],[{"start":8,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":29,"cssClass":"pl-en"},{"start":30,"end":40,"cssClass":"pl-v"}],[{"start":8,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":31,"cssClass":"pl-en"},{"start":32,"end":39,"cssClass":"pl-s1"},{"start":41,"end":45,"cssClass":"pl-s1"},{"start":46,"end":54,"cssClass":"pl-v"},{"start":55,"end":56,"cssClass":"pl-c1"},{"start":56,"end":57,"cssClass":"pl-c1"}],[{"start":8,"end":11,"cssClass":"pl-k"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-c1"},{"start":17,"end":22,"cssClass":"pl-en"},{"start":23,"end":27,"cssClass":"pl-s1"},{"start":28,"end":33,"cssClass":"pl-v"},{"start":34,"end":35,"cssClass":"pl-c1"},{"start":36,"end":37,"cssClass":"pl-c1"},{"start":39,"end":40,"cssClass":"pl-c1"},{"start":40,"end":41,"cssClass":"pl-c1"},{"start":43,"end":44,"cssClass":"pl-c1"},{"start":44,"end":45,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":28,"cssClass":"pl-s"},{"start":19,"end":21,"cssClass":"pl-cce"},{"start":30,"end":31,"cssClass":"pl-s1"},{"start":33,"end":37,"cssClass":"pl-s"},{"start":34,"end":36,"cssClass":"pl-cce"}],[{"start":12,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":27,"cssClass":"pl-s1"}],[{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":30,"cssClass":"pl-s"},{"start":32,"end":35,"cssClass":"pl-s1"}],[{"start":12,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":26,"cssClass":"pl-en"},{"start":27,"end":30,"cssClass":"pl-s1"},{"start":32,"end":36,"cssClass":"pl-s1"},{"start":36,"end":37,"cssClass":"pl-c1"},{"start":37,"end":42,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":47,"cssClass":"pl-s"},{"start":49,"end":52,"cssClass":"pl-s1"}],[{"start":12,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":26,"cssClass":"pl-en"},{"start":27,"end":30,"cssClass":"pl-s1"},{"start":32,"end":39,"cssClass":"pl-s1"},{"start":39,"end":40,"cssClass":"pl-c1"},{"start":40,"end":44,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":46,"cssClass":"pl-s"},{"start":48,"end":51,"cssClass":"pl-s1"}],[{"start":12,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":29,"cssClass":"pl-en"},{"start":30,"end":33,"cssClass":"pl-s1"},{"start":35,"end":39,"cssClass":"pl-s1"},{"start":40,"end":48,"cssClass":"pl-v"},{"start":49,"end":50,"cssClass":"pl-s1"}],[{"start":12,"end":14,"cssClass":"pl-k"},{"start":16,"end":17,"cssClass":"pl-s1"},{"start":18,"end":20,"cssClass":"pl-c1"},{"start":21,"end":22,"cssClass":"pl-c1"}],[{"start":16,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":38,"cssClass":"pl-en"},{"start":39,"end":42,"cssClass":"pl-s1"}],[{"start":16,"end":21,"cssClass":"pl-en"},{"start":22,"end":49,"cssClass":"pl-s"},{"start":51,"end":54,"cssClass":"pl-s1"}],[{"start":12,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":27,"cssClass":"pl-s1"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":24,"cssClass":"pl-s1"}],[],[{"start":4,"end":31,"cssClass":"pl-c"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":20,"cssClass":"pl-en"},{"start":21,"end":25,"cssClass":"pl-s1"},{"start":27,"end":31,"cssClass":"pl-s1"}],[{"start":8,"end":14,"cssClass":"pl-s1"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":23,"end":24,"cssClass":"pl-c1"}],[{"start":8,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":18,"cssClass":"pl-c1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":12,"end":18,"cssClass":"pl-s1"},{"start":19,"end":21,"cssClass":"pl-c1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":27,"cssClass":"pl-c1"},{"start":28,"end":34,"cssClass":"pl-s1"},{"start":35,"end":37,"cssClass":"pl-c1"},{"start":38,"end":43,"cssClass":"pl-s1"},{"start":44,"end":45,"cssClass":"pl-c1"},{"start":46,"end":47,"cssClass":"pl-c1"}],[{"start":12,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":22,"cssClass":"pl-s1"},{"start":23,"end":28,"cssClass":"pl-s1"},{"start":29,"end":30,"cssClass":"pl-c1"},{"start":31,"end":37,"cssClass":"pl-s1"}],[{"start":12,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":27,"cssClass":"pl-s1"},{"start":28,"end":33,"cssClass":"pl-en"},{"start":34,"end":40,"cssClass":"pl-s1"}],[{"start":12,"end":14,"cssClass":"pl-k"},{"start":16,"end":25,"cssClass":"pl-s1"},{"start":26,"end":28,"cssClass":"pl-c1"},{"start":29,"end":35,"cssClass":"pl-s1"}],[{"start":16,"end":22,"cssClass":"pl-k"},{"start":23,"end":27,"cssClass":"pl-s1"},{"start":29,"end":34,"cssClass":"pl-s1"},{"start":35,"end":36,"cssClass":"pl-c1"},{"start":37,"end":43,"cssClass":"pl-s1"}],[{"start":12,"end":18,"cssClass":"pl-k"},{"start":19,"end":23,"cssClass":"pl-s1"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":19,"cssClass":"pl-s1"}],[],[{"start":4,"end":16,"cssClass":"pl-c"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":15,"cssClass":"pl-en"},{"start":16,"end":20,"cssClass":"pl-s1"},{"start":22,"end":25,"cssClass":"pl-v"},{"start":27,"end":31,"cssClass":"pl-v"},{"start":33,"end":37,"cssClass":"pl-s1"},{"start":37,"end":38,"cssClass":"pl-c1"},{"start":38,"end":43,"cssClass":"pl-s"}],[{"start":8,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":23,"cssClass":"pl-s1"},{"start":24,"end":36,"cssClass":"pl-en"},{"start":37,"end":41,"cssClass":"pl-v"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":33,"cssClass":"pl-s"},{"start":34,"end":42,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":26,"cssClass":"pl-en"},{"start":27,"end":30,"cssClass":"pl-v"}],[{"start":8,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":23,"cssClass":"pl-s"}],[{"start":8,"end":11,"cssClass":"pl-k"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-c1"},{"start":17,"end":25,"cssClass":"pl-s1"}],[{"start":12,"end":25,"cssClass":"pl-s1"},{"start":26,"end":27,"cssClass":"pl-c1"},{"start":28,"end":32,"cssClass":"pl-s1"},{"start":33,"end":49,"cssClass":"pl-en"},{"start":50,"end":51,"cssClass":"pl-s1"}],[{"start":12,"end":23,"cssClass":"pl-s1"},{"start":24,"end":25,"cssClass":"pl-c1"},{"start":26,"end":30,"cssClass":"pl-en"},{"start":31,"end":33,"cssClass":"pl-s1"},{"start":34,"end":39,"cssClass":"pl-en"},{"start":40,"end":53,"cssClass":"pl-s1"},{"start":55,"end":62,"cssClass":"pl-en"},{"start":63,"end":64,"cssClass":"pl-c1"},{"start":64,"end":65,"cssClass":"pl-c1"}],[{"start":12,"end":15,"cssClass":"pl-k"},{"start":16,"end":17,"cssClass":"pl-s1"},{"start":18,"end":20,"cssClass":"pl-c1"},{"start":21,"end":32,"cssClass":"pl-s1"}],[{"start":16,"end":26,"cssClass":"pl-s1"},{"start":27,"end":29,"cssClass":"pl-c1"},{"start":30,"end":40,"cssClass":"pl-s"},{"start":32,"end":39,"cssClass":"pl-s1"},{"start":32,"end":33,"cssClass":"pl-kos"},{"start":33,"end":34,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-kos"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":21,"cssClass":"pl-v"},{"start":22,"end":23,"cssClass":"pl-c1"}],[{"start":8,"end":20,"cssClass":"pl-c"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":12,"end":16,"cssClass":"pl-s1"},{"start":17,"end":19,"cssClass":"pl-c1"},{"start":20,"end":25,"cssClass":"pl-s"}],[{"start":12,"end":18,"cssClass":"pl-k"},{"start":19,"end":28,"cssClass":"pl-en"},{"start":29,"end":34,"cssClass":"pl-s1"},{"start":35,"end":42,"cssClass":"pl-en"},{"start":43,"end":53,"cssClass":"pl-s1"},{"start":56,"end":62,"cssClass":"pl-en"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":12,"end":16,"cssClass":"pl-s1"},{"start":17,"end":19,"cssClass":"pl-c1"},{"start":20,"end":24,"cssClass":"pl-s"}],[{"start":12,"end":18,"cssClass":"pl-k"},{"start":19,"end":47,"cssClass":"pl-s"},{"start":21,"end":46,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-kos"},{"start":22,"end":25,"cssClass":"pl-en"},{"start":26,"end":36,"cssClass":"pl-s1"},{"start":38,"end":40,"cssClass":"pl-c1"},{"start":45,"end":46,"cssClass":"pl-kos"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":12,"end":16,"cssClass":"pl-s1"},{"start":17,"end":19,"cssClass":"pl-c1"},{"start":20,"end":29,"cssClass":"pl-s"}],[{"start":12,"end":18,"cssClass":"pl-k"}],[{"start":16,"end":21,"cssClass":"pl-s"},{"start":23,"end":33,"cssClass":"pl-s1"}],[{"start":16,"end":21,"cssClass":"pl-s"},{"start":23,"end":32,"cssClass":"pl-en"},{"start":33,"end":38,"cssClass":"pl-s1"},{"start":39,"end":46,"cssClass":"pl-en"},{"start":47,"end":57,"cssClass":"pl-s1"},{"start":60,"end":66,"cssClass":"pl-en"}],[{"start":16,"end":20,"cssClass":"pl-s"},{"start":22,"end":25,"cssClass":"pl-en"},{"start":26,"end":29,"cssClass":"pl-en"},{"start":30,"end":40,"cssClass":"pl-s1"},{"start":42,"end":44,"cssClass":"pl-c1"},{"start":47,"end":48,"cssClass":"pl-c1"},{"start":51,"end":56,"cssClass":"pl-en"},{"start":57,"end":60,"cssClass":"pl-en"},{"start":61,"end":71,"cssClass":"pl-s1"},{"start":73,"end":74,"cssClass":"pl-c1"},{"start":75,"end":76,"cssClass":"pl-c1"}],[],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":25,"cssClass":"pl-s1"}],[],[{"start":4,"end":16,"cssClass":"pl-c"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":15,"cssClass":"pl-en"},{"start":16,"end":20,"cssClass":"pl-s1"},{"start":22,"end":25,"cssClass":"pl-v"},{"start":27,"end":33,"cssClass":"pl-v"},{"start":35,"end":39,"cssClass":"pl-s1"},{"start":39,"end":40,"cssClass":"pl-c1"},{"start":40,"end":45,"cssClass":"pl-s"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":15,"cssClass":"pl-s1"},{"start":16,"end":18,"cssClass":"pl-c1"},{"start":20,"end":25,"cssClass":"pl-s"},{"start":27,"end":31,"cssClass":"pl-s"},{"start":33,"end":38,"cssClass":"pl-s"}],[{"start":12,"end":16,"cssClass":"pl-s1"},{"start":17,"end":30,"cssClass":"pl-en"},{"start":31,"end":34,"cssClass":"pl-v"}],[{"start":12,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":21,"cssClass":"pl-s"}],[],[{"start":12,"end":14,"cssClass":"pl-k"},{"start":16,"end":20,"cssClass":"pl-s1"},{"start":21,"end":23,"cssClass":"pl-c1"},{"start":24,"end":29,"cssClass":"pl-s"}],[{"start":16,"end":22,"cssClass":"pl-v"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":25,"end":34,"cssClass":"pl-en"},{"start":35,"end":41,"cssClass":"pl-v"},{"start":43,"end":46,"cssClass":"pl-en"}],[{"start":16,"end":21,"cssClass":"pl-en"},{"start":22,"end":37,"cssClass":"pl-s"},{"start":38,"end":44,"cssClass":"pl-v"}],[{"start":12,"end":14,"cssClass":"pl-k"},{"start":16,"end":20,"cssClass":"pl-s1"},{"start":21,"end":23,"cssClass":"pl-c1"},{"start":24,"end":28,"cssClass":"pl-s"}],[{"start":16,"end":22,"cssClass":"pl-v"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":25,"end":28,"cssClass":"pl-en"},{"start":29,"end":32,"cssClass":"pl-en"},{"start":33,"end":39,"cssClass":"pl-v"},{"start":41,"end":42,"cssClass":"pl-c1"},{"start":45,"end":52,"cssClass":"pl-en"},{"start":53,"end":57,"cssClass":"pl-s"},{"start":59,"end":61,"cssClass":"pl-s"}],[{"start":16,"end":21,"cssClass":"pl-en"},{"start":22,"end":36,"cssClass":"pl-s"},{"start":37,"end":43,"cssClass":"pl-v"}],[{"start":12,"end":14,"cssClass":"pl-k"},{"start":16,"end":19,"cssClass":"pl-en"},{"start":20,"end":26,"cssClass":"pl-v"},{"start":28,"end":29,"cssClass":"pl-c1"},{"start":30,"end":32,"cssClass":"pl-c1"},{"start":33,"end":35,"cssClass":"pl-c1"},{"start":36,"end":37,"cssClass":"pl-c1"},{"start":38,"end":41,"cssClass":"pl-c1"},{"start":42,"end":45,"cssClass":"pl-en"},{"start":46,"end":52,"cssClass":"pl-v"},{"start":54,"end":55,"cssClass":"pl-c1"},{"start":56,"end":57,"cssClass":"pl-c1"}],[{"start":16,"end":23,"cssClass":"pl-s1"},{"start":24,"end":25,"cssClass":"pl-c1"},{"start":26,"end":32,"cssClass":"pl-v"}],[{"start":16,"end":21,"cssClass":"pl-k"},{"start":23,"end":26,"cssClass":"pl-en"},{"start":27,"end":34,"cssClass":"pl-s1"},{"start":36,"end":38,"cssClass":"pl-c1"},{"start":39,"end":40,"cssClass":"pl-c1"}],[{"start":20,"end":32,"cssClass":"pl-s1"},{"start":33,"end":34,"cssClass":"pl-c1"},{"start":35,"end":39,"cssClass":"pl-s1"},{"start":40,"end":56,"cssClass":"pl-en"},{"start":57,"end":64,"cssClass":"pl-s1"},{"start":66,"end":68,"cssClass":"pl-c1"}],[{"start":20,"end":29,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-c1"},{"start":32,"end":36,"cssClass":"pl-en"},{"start":37,"end":39,"cssClass":"pl-s1"},{"start":40,"end":45,"cssClass":"pl-en"},{"start":46,"end":58,"cssClass":"pl-s1"},{"start":60,"end":67,"cssClass":"pl-en"},{"start":68,"end":69,"cssClass":"pl-c1"},{"start":69,"end":70,"cssClass":"pl-c1"}],[{"start":20,"end":29,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-c1"},{"start":32,"end":36,"cssClass":"pl-s1"},{"start":37,"end":49,"cssClass":"pl-en"},{"start":50,"end":59,"cssClass":"pl-s1"}],[{"start":20,"end":23,"cssClass":"pl-k"},{"start":24,"end":25,"cssClass":"pl-s1"},{"start":26,"end":28,"cssClass":"pl-c1"},{"start":29,"end":38,"cssClass":"pl-s1"}],[{"start":24,"end":28,"cssClass":"pl-s1"},{"start":29,"end":31,"cssClass":"pl-c1"},{"start":32,"end":35,"cssClass":"pl-en"},{"start":36,"end":37,"cssClass":"pl-s1"}],[{"start":20,"end":22,"cssClass":"pl-k"},{"start":24,"end":27,"cssClass":"pl-en"},{"start":28,"end":35,"cssClass":"pl-s1"},{"start":37,"end":39,"cssClass":"pl-c1"},{"start":40,"end":42,"cssClass":"pl-c1"}],[{"start":24,"end":31,"cssClass":"pl-s1"},{"start":32,"end":33,"cssClass":"pl-c1"},{"start":34,"end":36,"cssClass":"pl-s"}],[{"start":20,"end":24,"cssClass":"pl-k"}],[{"start":24,"end":31,"cssClass":"pl-s1"},{"start":32,"end":33,"cssClass":"pl-c1"},{"start":34,"end":41,"cssClass":"pl-s1"},{"start":42,"end":44,"cssClass":"pl-c1"}],[{"start":16,"end":20,"cssClass":"pl-s1"},{"start":21,"end":29,"cssClass":"pl-v"},{"start":30,"end":31,"cssClass":"pl-c1"}],[{"start":16,"end":22,"cssClass":"pl-k"},{"start":23,"end":27,"cssClass":"pl-s1"}],[],[{"start":12,"end":16,"cssClass":"pl-k"}],[{"start":16,"end":21,"cssClass":"pl-k"},{"start":22,"end":31,"cssClass":"pl-v"},{"start":32,"end":88,"cssClass":"pl-s"},{"start":39,"end":47,"cssClass":"pl-s1"},{"start":39,"end":40,"cssClass":"pl-kos"},{"start":40,"end":46,"cssClass":"pl-v"},{"start":46,"end":47,"cssClass":"pl-kos"}],[],[{"start":8,"end":12,"cssClass":"pl-k"}],[{"start":12,"end":17,"cssClass":"pl-k"},{"start":18,"end":27,"cssClass":"pl-v"},{"start":28,"end":76,"cssClass":"pl-s"},{"start":68,"end":74,"cssClass":"pl-s1"},{"start":68,"end":69,"cssClass":"pl-kos"},{"start":69,"end":73,"cssClass":"pl-s1"},{"start":73,"end":74,"cssClass":"pl-kos"}],[],[],[{"start":0,"end":2,"cssClass":"pl-k"},{"start":4,"end":12,"cssClass":"pl-s1"},{"start":13,"end":15,"cssClass":"pl-c1"},{"start":16,"end":26,"cssClass":"pl-s"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":16,"cssClass":"pl-v"}],[{"start":4,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":44,"cssClass":"pl-s"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":51,"cssClass":"pl-s"}],[{"start":4,"end":18,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":19,"end":24,"cssClass":"pl-en"},{"start":25,"end":57,"cssClass":"pl-s"},{"start":58,"end":59,"cssClass":"pl-c1"},{"start":59,"end":65,"cssClass":"pl-s"}],[],[{"start":4,"end":8,"cssClass":"pl-k"},{"start":9,"end":13,"cssClass":"pl-en"},{"start":14,"end":28,"cssClass":"pl-s1"},{"start":30,"end":34,"cssClass":"pl-s"},{"start":36,"end":38,"cssClass":"pl-k"},{"start":39,"end":47,"cssClass":"pl-s1"}],[{"start":8,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":24,"cssClass":"pl-s1"},{"start":25,"end":34,"cssClass":"pl-en"},{"start":35,"end":43,"cssClass":"pl-s1"},{"start":44,"end":48,"cssClass":"pl-en"}],[{"start":8,"end":22,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":23,"end":30,"cssClass":"pl-s1"},{"start":31,"end":37,"cssClass":"pl-en"},{"start":38,"end":45,"cssClass":"pl-s"}],[{"start":4,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":15,"end":23,"cssClass":"pl-s1"},{"start":24,"end":32,"cssClass":"pl-s1"},{"start":33,"end":36,"cssClass":"pl-en"}],[{"start":4,"end":5,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":7,"end":13,"cssClass":"pl-s1"},{"start":14,"end":21,"cssClass":"pl-en"},{"start":22,"end":25,"cssClass":"pl-s1"},{"start":26,"end":40,"cssClass":"pl-s1"},{"start":41,"end":45,"cssClass":"pl-s"}],[{"start":4,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":15,"end":23,"cssClass":"pl-s1"},{"start":24,"end":32,"cssClass":"pl-s1"},{"start":33,"end":36,"cssClass":"pl-en"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":29,"cssClass":"pl-s"},{"start":32,"end":40,"cssClass":"pl-s1"},{"start":41,"end":42,"cssClass":"pl-c1"},{"start":43,"end":51,"cssClass":"pl-s1"},{"start":53,"end":65,"cssClass":"pl-s1"},{"start":66,"end":67,"cssClass":"pl-c1"},{"start":68,"end":72,"cssClass":"pl-c1"},{"start":74,"end":90,"cssClass":"pl-s"}],[{"start":4,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":30,"cssClass":"pl-s1"},{"start":31,"end":40,"cssClass":"pl-en"},{"start":41,"end":42,"cssClass":"pl-s1"}],[{"start":4,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":23,"cssClass":"pl-en"},{"start":24,"end":45,"cssClass":"pl-s"},{"start":47,"end":51,"cssClass":"pl-s"}],[{"start":4,"end":16,"cssClass":"pl-s1"},{"start":17,"end":22,"cssClass":"pl-en"},{"start":23,"end":40,"cssClass":"pl-s1"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":48,"cssClass":"pl-s"}],[],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":51,"cssClass":"pl-s"}],[{"start":4,"end":19,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":20,"end":25,"cssClass":"pl-en"},{"start":26,"end":52,"cssClass":"pl-s"},{"start":53,"end":54,"cssClass":"pl-c1"},{"start":54,"end":60,"cssClass":"pl-s"}],[{"start":4,"end":8,"cssClass":"pl-k"},{"start":9,"end":13,"cssClass":"pl-en"},{"start":14,"end":29,"cssClass":"pl-s1"},{"start":31,"end":35,"cssClass":"pl-s"},{"start":37,"end":39,"cssClass":"pl-k"},{"start":40,"end":48,"cssClass":"pl-s1"}],[{"start":8,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":19,"cssClass":"pl-s1"},{"start":20,"end":29,"cssClass":"pl-en"},{"start":30,"end":38,"cssClass":"pl-s1"},{"start":39,"end":43,"cssClass":"pl-en"}],[{"start":4,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":24,"cssClass":"pl-s1"},{"start":25,"end":33,"cssClass":"pl-s1"},{"start":34,"end":37,"cssClass":"pl-en"}],[{"start":4,"end":5,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":6,"end":12,"cssClass":"pl-s1"},{"start":13,"end":20,"cssClass":"pl-en"},{"start":21,"end":24,"cssClass":"pl-s1"},{"start":25,"end":27,"cssClass":"pl-s1"},{"start":28,"end":32,"cssClass":"pl-s"}],[{"start":4,"end":14,"cssClass":"pl-s1"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":17,"end":25,"cssClass":"pl-s1"},{"start":26,"end":34,"cssClass":"pl-s1"},{"start":35,"end":38,"cssClass":"pl-en"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":29,"cssClass":"pl-s"},{"start":32,"end":42,"cssClass":"pl-s1"},{"start":42,"end":43,"cssClass":"pl-c1"},{"start":44,"end":53,"cssClass":"pl-s1"},{"start":55,"end":67,"cssClass":"pl-s1"},{"start":68,"end":69,"cssClass":"pl-c1"},{"start":70,"end":74,"cssClass":"pl-c1"},{"start":76,"end":92,"cssClass":"pl-s"}],[{"start":4,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":30,"cssClass":"pl-s1"},{"start":31,"end":40,"cssClass":"pl-en"},{"start":41,"end":42,"cssClass":"pl-s1"}],[{"start":4,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":24,"cssClass":"pl-en"},{"start":25,"end":46,"cssClass":"pl-s"},{"start":48,"end":52,"cssClass":"pl-s"}],[{"start":4,"end":17,"cssClass":"pl-s1"},{"start":18,"end":23,"cssClass":"pl-en"},{"start":24,"end":41,"cssClass":"pl-s1"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":51,"cssClass":"pl-s"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":48,"cssClass":"pl-s"}],[]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/helmii18/encrypt-decrypt-pdf-file-with-AES256-/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false,"repoAlertsPath":"/helmii18/encrypt-decrypt-pdf-file-with-AES256-/security/dependabot","repoSecurityAndAnalysisPath":"/helmii18/encrypt-decrypt-pdf-file-with-AES256-/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"AES256.py","displayUrl":"https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/blob/main/AES256.py?raw=true","headerInfo":{"blobSize":"26.9 KB","deleteInfo":{"deleteTooltip":"Fork this repository and delete the file"},"editInfo":{"editTooltip":"Fork this repository and edit the file"},"ghDesktopPath":"x-github-client://openRepo/https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-?branch=main\u0026filepath=AES256.py","gitLfsPath":null,"onBranch":true,"shortPath":"22079bc","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fhelmii18%2Fencrypt-decrypt-pdf-file-with-AES256-%2Fblob%2Fmain%2FAES256.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"585","truncatedSloc":"518"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":true,"newDiscussionPath":"/helmii18/encrypt-decrypt-pdf-file-with-AES256-/discussions/new","newIssuePath":"/helmii18/encrypt-decrypt-pdf-file-with-AES256-/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/helmii18/encrypt-decrypt-pdf-file-with-AES256-/blob/main/AES256.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/helmii18/encrypt-decrypt-pdf-file-with-AES256-/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/raw/main/AES256.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"helmii18","repoName":"encrypt-decrypt-pdf-file-with-AES256-","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"roundConstant","kind":"constant","ident_start":90,"ident_end":103,"extent_start":90,"extent_end":419,"fully_qualified_name":"roundConstant","ident_utf16":{"start":{"line_number":5,"utf16_col":0},"end":{"line_number":5,"utf16_col":13}},"extent_utf16":{"start":{"line_number":5,"utf16_col":0},"end":{"line_number":16,"utf16_col":2}}},{"name":"roundConstant_8","kind":"constant","ident_start":421,"ident_end":436,"extent_start":421,"extent_end":992,"fully_qualified_name":"roundConstant_8","ident_utf16":{"start":{"line_number":18,"utf16_col":0},"end":{"line_number":18,"utf16_col":15}},"extent_utf16":{"start":{"line_number":18,"utf16_col":0},"end":{"line_number":29,"utf16_col":2}}},{"name":"s_box","kind":"constant","ident_start":1026,"ident_end":1031,"extent_start":1026,"extent_end":2679,"fully_qualified_name":"s_box","ident_utf16":{"start":{"line_number":33,"utf16_col":0},"end":{"line_number":33,"utf16_col":5}},"extent_utf16":{"start":{"line_number":33,"utf16_col":0},"end":{"line_number":50,"utf16_col":2}}},{"name":"invs_box","kind":"constant","ident_start":2713,"ident_end":2721,"extent_start":2713,"extent_end":4369,"fully_qualified_name":"invs_box","ident_utf16":{"start":{"line_number":54,"utf16_col":0},"end":{"line_number":54,"utf16_col":8}},"extent_utf16":{"start":{"line_number":54,"utf16_col":0},"end":{"line_number":71,"utf16_col":2}}},{"name":"encryptMDS","kind":"constant","ident_start":4408,"ident_end":4418,"extent_start":4408,"extent_end":4554,"fully_qualified_name":"encryptMDS","ident_utf16":{"start":{"line_number":75,"utf16_col":0},"end":{"line_number":75,"utf16_col":10}},"extent_utf16":{"start":{"line_number":75,"utf16_col":0},"end":{"line_number":80,"utf16_col":2}}},{"name":"encryptMDS_8","kind":"constant","ident_start":4597,"ident_end":4609,"extent_start":4597,"extent_end":5057,"fully_qualified_name":"encryptMDS_8","ident_utf16":{"start":{"line_number":84,"utf16_col":0},"end":{"line_number":84,"utf16_col":12}},"extent_utf16":{"start":{"line_number":84,"utf16_col":0},"end":{"line_number":93,"utf16_col":2}}},{"name":"decryptMDS","kind":"constant","ident_start":5096,"ident_end":5106,"extent_start":5096,"extent_end":5242,"fully_qualified_name":"decryptMDS","ident_utf16":{"start":{"line_number":97,"utf16_col":0},"end":{"line_number":97,"utf16_col":10}},"extent_utf16":{"start":{"line_number":97,"utf16_col":0},"end":{"line_number":102,"utf16_col":2}}},{"name":"decryptMDS_8","kind":"constant","ident_start":5284,"ident_end":5296,"extent_start":5284,"extent_end":5744,"fully_qualified_name":"decryptMDS_8","ident_utf16":{"start":{"line_number":105,"utf16_col":0},"end":{"line_number":105,"utf16_col":12}},"extent_utf16":{"start":{"line_number":105,"utf16_col":0},"end":{"line_number":114,"utf16_col":2}}},{"name":"mc2","kind":"constant","ident_start":5775,"ident_end":5778,"extent_start":5775,"extent_end":7425,"fully_qualified_name":"mc2","ident_utf16":{"start":{"line_number":118,"utf16_col":0},"end":{"line_number":118,"utf16_col":3}},"extent_utf16":{"start":{"line_number":118,"utf16_col":0},"end":{"line_number":135,"utf16_col":2}}},{"name":"mc3","kind":"constant","ident_start":7428,"ident_end":7431,"extent_start":7428,"extent_end":9078,"fully_qualified_name":"mc3","ident_utf16":{"start":{"line_number":138,"utf16_col":0},"end":{"line_number":138,"utf16_col":3}},"extent_utf16":{"start":{"line_number":138,"utf16_col":0},"end":{"line_number":155,"utf16_col":2}}},{"name":"mc9","kind":"constant","ident_start":9081,"ident_end":9084,"extent_start":9081,"extent_end":10731,"fully_qualified_name":"mc9","ident_utf16":{"start":{"line_number":158,"utf16_col":0},"end":{"line_number":158,"utf16_col":3}},"extent_utf16":{"start":{"line_number":158,"utf16_col":0},"end":{"line_number":175,"utf16_col":2}}},{"name":"mc11","kind":"constant","ident_start":10740,"ident_end":10744,"extent_start":10740,"extent_end":12391,"fully_qualified_name":"mc11","ident_utf16":{"start":{"line_number":178,"utf16_col":0},"end":{"line_number":178,"utf16_col":4}},"extent_utf16":{"start":{"line_number":178,"utf16_col":0},"end":{"line_number":195,"utf16_col":2}}},{"name":"mc13","kind":"constant","ident_start":12401,"ident_end":12405,"extent_start":12401,"extent_end":14052,"fully_qualified_name":"mc13","ident_utf16":{"start":{"line_number":199,"utf16_col":0},"end":{"line_number":199,"utf16_col":4}},"extent_utf16":{"start":{"line_number":199,"utf16_col":0},"end":{"line_number":216,"utf16_col":2}}},{"name":"mc14","kind":"constant","ident_start":14062,"ident_end":14066,"extent_start":14062,"extent_end":15713,"fully_qualified_name":"mc14","ident_utf16":{"start":{"line_number":220,"utf16_col":0},"end":{"line_number":220,"utf16_col":4}},"extent_utf16":{"start":{"line_number":220,"utf16_col":0},"end":{"line_number":237,"utf16_col":2}}},{"name":"keyToHexArray","kind":"function","ident_start":15737,"ident_end":15750,"extent_start":15733,"extent_end":15913,"fully_qualified_name":"keyToHexArray","ident_utf16":{"start":{"line_number":242,"utf16_col":4},"end":{"line_number":242,"utf16_col":17}},"extent_utf16":{"start":{"line_number":242,"utf16_col":0},"end":{"line_number":248,"utf16_col":14}}},{"name":"arrayShift","kind":"function","ident_start":15949,"ident_end":15959,"extent_start":15945,"extent_end":16006,"fully_qualified_name":"arrayShift","ident_utf16":{"start":{"line_number":252,"utf16_col":4},"end":{"line_number":252,"utf16_col":14}},"extent_utf16":{"start":{"line_number":252,"utf16_col":0},"end":{"line_number":253,"utf16_col":30}}},{"name":"arraySbox","kind":"function","ident_start":16033,"ident_end":16042,"extent_start":16029,"extent_end":16204,"fully_qualified_name":"arraySbox","ident_utf16":{"start":{"line_number":257,"utf16_col":4},"end":{"line_number":257,"utf16_col":13}},"extent_utf16":{"start":{"line_number":257,"utf16_col":0},"end":{"line_number":262,"utf16_col":14}}},{"name":"arrayInvSbox","kind":"function","ident_start":16239,"ident_end":16251,"extent_start":16235,"extent_end":16416,"fully_qualified_name":"arrayInvSbox","ident_utf16":{"start":{"line_number":266,"utf16_col":4},"end":{"line_number":266,"utf16_col":16}},"extent_utf16":{"start":{"line_number":266,"utf16_col":0},"end":{"line_number":271,"utf16_col":14}}},{"name":"xorArray","kind":"function","ident_start":16478,"ident_end":16486,"extent_start":16474,"extent_end":17214,"fully_qualified_name":"xorArray","ident_utf16":{"start":{"line_number":275,"utf16_col":4},"end":{"line_number":275,"utf16_col":12}},"extent_utf16":{"start":{"line_number":275,"utf16_col":0},"end":{"line_number":294,"utf16_col":20}}},{"name":"addRoundKey","kind":"function","ident_start":17238,"ident_end":17249,"extent_start":17234,"extent_end":17300,"fully_qualified_name":"addRoundKey","ident_utf16":{"start":{"line_number":298,"utf16_col":4},"end":{"line_number":298,"utf16_col":15}},"extent_utf16":{"start":{"line_number":298,"utf16_col":0},"end":{"line_number":299,"utf16_col":37}}},{"name":"subBytes","kind":"function","ident_start":17338,"ident_end":17346,"extent_start":17334,"extent_end":17493,"fully_qualified_name":"subBytes","ident_utf16":{"start":{"line_number":303,"utf16_col":4},"end":{"line_number":303,"utf16_col":12}},"extent_utf16":{"start":{"line_number":303,"utf16_col":0},"end":{"line_number":309,"utf16_col":14}}},{"name":"shiftRow","kind":"function","ident_start":17524,"ident_end":17532,"extent_start":17520,"extent_end":17919,"fully_qualified_name":"shiftRow","ident_utf16":{"start":{"line_number":313,"utf16_col":4},"end":{"line_number":313,"utf16_col":12}},"extent_utf16":{"start":{"line_number":313,"utf16_col":0},"end":{"line_number":322,"utf16_col":36}}},{"name":"mixColumn","kind":"function","ident_start":17939,"ident_end":17948,"extent_start":17935,"extent_end":18657,"fully_qualified_name":"mixColumn","ident_utf16":{"start":{"line_number":326,"utf16_col":4},"end":{"line_number":326,"utf16_col":13}},"extent_utf16":{"start":{"line_number":326,"utf16_col":0},"end":{"line_number":343,"utf16_col":32}}},{"name":"inverseMixColumn","kind":"function","ident_start":18685,"ident_end":18701,"extent_start":18681,"extent_end":19614,"fully_qualified_name":"inverseMixColumn","ident_utf16":{"start":{"line_number":347,"utf16_col":4},"end":{"line_number":347,"utf16_col":20}},"extent_utf16":{"start":{"line_number":347,"utf16_col":0},"end":{"line_number":368,"utf16_col":32}}},{"name":"hexToMatrix","kind":"function","ident_start":19777,"ident_end":19788,"extent_start":19773,"extent_end":20133,"fully_qualified_name":"hexToMatrix","ident_utf16":{"start":{"line_number":378,"utf16_col":4},"end":{"line_number":378,"utf16_col":15}},"extent_utf16":{"start":{"line_number":378,"utf16_col":0},"end":{"line_number":387,"utf16_col":54}}},{"name":"AES","kind":"class","ident_start":20141,"ident_end":20144,"extent_start":20135,"extent_end":26075,"fully_qualified_name":"AES","ident_utf16":{"start":{"line_number":389,"utf16_col":6},"end":{"line_number":389,"utf16_col":9}},"extent_utf16":{"start":{"line_number":389,"utf16_col":0},"end":{"line_number":550,"utf16_col":77}}},{"name":"__init__","kind":"function","ident_start":20155,"ident_end":20163,"extent_start":20151,"extent_end":20221,"fully_qualified_name":"AES.__init__","ident_utf16":{"start":{"line_number":391,"utf16_col":8},"end":{"line_number":391,"utf16_col":16}},"extent_utf16":{"start":{"line_number":391,"utf16_col":4},"end":{"line_number":393,"utf16_col":26}}},{"name":"__keySchedule","kind":"function","ident_start":20252,"ident_end":20265,"extent_start":20248,"extent_end":21272,"fully_qualified_name":"AES.__keySchedule","ident_utf16":{"start":{"line_number":396,"utf16_col":8},"end":{"line_number":396,"utf16_col":21}},"extent_utf16":{"start":{"line_number":396,"utf16_col":4},"end":{"line_number":417,"utf16_col":32}}},{"name":"__convertRoundKey","kind":"function","ident_start":21326,"ident_end":21343,"extent_start":21322,"extent_end":21547,"fully_qualified_name":"AES.__convertRoundKey","ident_utf16":{"start":{"line_number":420,"utf16_col":8},"end":{"line_number":420,"utf16_col":25}},"extent_utf16":{"start":{"line_number":420,"utf16_col":4},"end":{"line_number":425,"utf16_col":28}}},{"name":"__encryptProcess","kind":"function","ident_start":21582,"ident_end":21598,"extent_start":21578,"extent_end":22344,"fully_qualified_name":"AES.__encryptProcess","ident_utf16":{"start":{"line_number":428,"utf16_col":8},"end":{"line_number":428,"utf16_col":24}},"extent_utf16":{"start":{"line_number":428,"utf16_col":4},"end":{"line_number":447,"utf16_col":25}}},{"name":"__addPadding","kind":"function","ident_start":22383,"ident_end":22395,"extent_start":22379,"extent_end":22754,"fully_qualified_name":"AES.__addPadding","ident_utf16":{"start":{"line_number":450,"utf16_col":8},"end":{"line_number":450,"utf16_col":20}},"extent_utf16":{"start":{"line_number":450,"utf16_col":4},"end":{"line_number":461,"utf16_col":23}}},{"name":"__decryptProcess","kind":"function","ident_start":22789,"ident_end":22805,"extent_start":22785,"extent_end":23506,"fully_qualified_name":"AES.__decryptProcess","ident_utf16":{"start":{"line_number":464,"utf16_col":8},"end":{"line_number":464,"utf16_col":24}},"extent_utf16":{"start":{"line_number":464,"utf16_col":4},"end":{"line_number":480,"utf16_col":24}}},{"name":"__delPadding","kind":"function","ident_start":23548,"ident_end":23560,"extent_start":23544,"extent_end":23877,"fully_qualified_name":"AES.__delPadding","ident_utf16":{"start":{"line_number":483,"utf16_col":8},"end":{"line_number":483,"utf16_col":20}},"extent_utf16":{"start":{"line_number":483,"utf16_col":4},"end":{"line_number":492,"utf16_col":19}}},{"name":"encrypt","kind":"function","ident_start":23904,"ident_end":23911,"extent_start":23900,"extent_end":24801,"fully_qualified_name":"AES.encrypt","ident_utf16":{"start":{"line_number":495,"utf16_col":8},"end":{"line_number":495,"utf16_col":15}},"extent_utf16":{"start":{"line_number":495,"utf16_col":4},"end":{"line_number":517,"utf16_col":25}}},{"name":"decrypt","kind":"function","ident_start":24828,"ident_end":24835,"extent_start":24824,"extent_end":26075,"fully_qualified_name":"AES.decrypt","ident_utf16":{"start":{"line_number":520,"utf16_col":8},"end":{"line_number":520,"utf16_col":15}},"extent_utf16":{"start":{"line_number":520,"utf16_col":4},"end":{"line_number":550,"utf16_col":77}}}]}},"copilotInfo":{"documentationUrl":"https://docs.github.com/copilot/overview-of-github-copilot/about-github-copilot-for-individuals","notices":{"codeViewPopover":{"dismissed":false,"dismissPath":"/settings/dismiss-notice/code_view_copilot_popover"}},"userAccess":{"accessAllowed":false,"hasSubscriptionEnded":false,"orgHasCFBAccess":false,"userHasCFIAccess":false,"userHasOrgs":false,"userIsOrgAdmin":false,"userIsOrgMember":false,"business":null,"featureRequestInfo":null}},"copilotAccessAllowed":false,"csrf_tokens":{"/helmii18/encrypt-decrypt-pdf-file-with-AES256-/branches":{"post":"pEmw_ukuyaXXtsdhx0csFzd01aFkkB0dSEHhryno9hOuK8TClh7QSUXvd_cpzALsBnnWFD_9_gzkVxjLZOX6GQ"},"/repos/preferences":{"post":"jJljdN9b8fMoksyfr6RDXdTWQZKRJDkOctgzMF62j2q_DiSQdlomlICscIh75yClxvfxsG5GRsdqlMZX5mx-ZA"}}},"title":"encrypt-decrypt-pdf-file-with-AES256-/AES256.py at main · helmii18/encrypt-decrypt-pdf-file-with-AES256-","appPayload":{"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-32bb159cc57c.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-c6704d501c10.js","githubDevUrl":"https://github.dev/","enabled_features":{"code_nav_ui_events":false,"copilot_conversational_ux":false,"copilot_conversational_ux_embedding_update":false,"copilot_popover_file_editor_header":true,"copilot_smell_icebreaker_ux":false,"copilot_workspace":false}}}</script>
  <div data-target="react-app.reactRoot"><meta data-hydrostats="publish"> <!-- --> <!-- --> <!-- --> <button hidden="" data-testid="header-permalink-button" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="y,Shift+Y"></button><button hidden="" data-hotkey="y,Shift+Y"></button><div class="Box-sc-g0xbh4-0"><div style="--sticky-pane-height: calc(100vh - (max(104px, 0px)));" class="Box-sc-g0xbh4-0 fSWWem"><div class="Box-sc-g0xbh4-0 kPPmzM"><div class="Box-sc-g0xbh4-0 cIAPDV"><div tabindex="0" class="Box-sc-g0xbh4-0 gvCnwW"><div class="Box-sc-g0xbh4-0 heUiss"><div class="Box-sc-g0xbh4-0 eUyHuk"></div><div style="--pane-width:320px" class="Box-sc-g0xbh4-0 gNdDUH"><div class="Box-sc-g0xbh4-0"><div id="repos-file-tree" class="Box-sc-g0xbh4-0 jyDQiw"><div class="Box-sc-g0xbh4-0 hBSSUC"><div class="Box-sc-g0xbh4-0 iPurHz"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 fNPcqd"><span role="tooltip" aria-label="Collapse file tree" id="expand-button-file-tree-button" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-se"><button data-component="IconButton" type="button" data-testid="collapse-file-tree-button" aria-labelledby="expand-button-file-tree-button" aria-expanded="true" aria-controls="repos-file-tree" class="types__StyledButton-sc-ws60qy-0 khvnOK" data-no-visuals="true" data-hotkey="Control+b"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-sidebar-expand" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.177 7.823 2.396-2.396A.25.25 0 0 1 7 5.604v4.792a.25.25 0 0 1-.427.177L4.177 8.177a.25.25 0 0 1 0-.354Z"></path><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25H9.5v-13Zm12.5 13a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11v13Z"></path></svg></button></span><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+b"></button></h2><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 imcwCi">Files</h2></div><div class="Box-sc-g0xbh4-0 hVHHYa"><div class="Box-sc-g0xbh4-0 idZfsJ"><button type="button" id="branch-picker-repos-header-ref-selector" aria-haspopup="true" tabindex="0" aria-label="main branch" data-testid="anchor-button" class="types__StyledButton-sc-ws60qy-0 kkhncB react-repos-tree-pane-ref-selector width-full ref-selector-class" data-hotkey="w"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text"><div class="Box-sc-g0xbh4-0 bKgizp"><div class="Box-sc-g0xbh4-0 dIAShY"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="Box-sc-g0xbh4-0 caeYDk ref-selector-button-text-container"><span class="Text-sc-17v1xeu-0 bOMzPg">&nbsp;<!-- -->main</span></div></div></span><span data-component="trailingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="w"></button></div><div class="Box-sc-g0xbh4-0 jahcnb"><span role="tooltip" aria-label="Add file" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-s"><a sx="[object Object]" data-component="IconButton" type="button" aria-label="Add file" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 kQvhRC" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/new/main"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-plus" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg></a></span><button data-component="IconButton" type="button" aria-label="Search this repository" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 bPGRMc" data-hotkey="/"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="/"></button></div></div></div><div class="Box-sc-g0xbh4-0 jRttMj"><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="t,Shift+T"></button><button hidden="" data-hotkey="t,Shift+T"></button><span class="TextInputWrapper__TextInputBaseWrapper-sc-1mqhpbi-0 TextInputWrapper-sc-1mqhpbi-1 bkmibs jxgrJS TextInput-wrapper" aria-busy="false"><span class="TextInput-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><input type="text" aria-label="Go to file" role="combobox" aria-controls="file-results-list" aria-expanded="false" aria-haspopup="dialog" autocorrect="off" spellcheck="false" placeholder="Go to file" data-component="input" class="UnstyledTextInput-sc-14ypya-0 cDLBls" value=""><span class="TextInput-icon"><div class="Box-sc-g0xbh4-0 cNvKlH"><kbd>t</kbd></div></span></span></div><div class="Box-sc-g0xbh4-0 bYLCoz"><div><div class="react-tree-show-tree-items"><div data-testid="repos-file-tree-container" class="Box-sc-g0xbh4-0 erWCJP"><nav aria-label="File Tree Navigation"><span role="status" aria-live="polite" aria-atomic="true" class="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0 rTZSs"></span><ul role="tree" aria-label="Files" class="TreeView__UlBox-sc-4ex6b6-0 dcpVHE"><li class="PRIVATE_TreeView-item" tabindex="0" id="AES256.py-item" role="treeitem" aria-labelledby=":ra:" aria-describedby=":rb: :rc:" aria-level="1" aria-current="true" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level: 1;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":ra:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":rb:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>AES256.py</span></span></div></div></li></ul></nav></div></div></div></div></div></div></div><div class="Box-sc-g0xbh4-0 jzJYzB"><div role="slider" aria-label="Draggable pane splitter" aria-valuemin="256" aria-valuemax="577" aria-valuenow="320" aria-valuetext="Pane width 320 pixels" tabindex="0" class="Box-sc-g0xbh4-0 bTSsYt"></div></div></div></div><div class="Box-sc-g0xbh4-0 emFMJu"><div class="Box-sc-g0xbh4-0"></div><div class="Box-sc-g0xbh4-0 hlUAHL"><div data-selector="repos-split-pane-content" tabindex="0" class="Box-sc-g0xbh4-0 iStsmI"><div class="Box-sc-g0xbh4-0 eIgvIk"><div class="Box-sc-g0xbh4-0 eVFfWF container"><div class="Box-sc-g0xbh4-0 kgXdnT react-code-view-header--narrow"><div class="Box-sc-g0xbh4-0 kzTa-dF"><div class="Box-sc-g0xbh4-0 bbXCl"><div class="Box-sc-g0xbh4-0 kIpapQ"><div class="Box-sc-g0xbh4-0 eTvGbF"><nav data-testid="breadcrumbs" aria-labelledby="repos-header-breadcrumb-mobile-heading" id="repos-header-breadcrumb-mobile" class="Box-sc-g0xbh4-0 kzRgrI"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading" id="repos-header-breadcrumb-mobile-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 cmAPIB"><li class="Box-sc-g0xbh4-0 jwXCBK"><a sx="[object Object]" data-testid="breadcrumbs-repo-link" class="Link__StyledLink-sc-14289xe-0 dpowyu" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/tree/main">encrypt-decrypt-pdf-file-with-AES256-</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 jwXCBK"><span aria-hidden="true" class="Text-sc-17v1xeu-0 ePvrxx">/</span><h1 tabindex="-1" id="file-name-id-mobile" class="Heading__StyledHeading-sc-1c1dgg0-0 diwsLq">AES256.py</h1></div><button data-component="IconButton" type="button" aria-label="Copy path" data-testid="breadcrumb-copy-path-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 IIGly"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button></div></div><div class="Box-sc-g0xbh4-0 hGGMNu"> <button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="l,Shift+L"></button><button hidden="" data-hotkey="l,Shift+L"></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Mod+Alt+g"></button><button hidden="" data-hotkey="Mod+Alt+g"></button><button type="button" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 bzquEC" data-hotkey="b,Shift+B,Control+/ Control+b"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text">Blame</span></span></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="b,Shift+B,Control+/ Control+b"></button><button data-component="IconButton" type="button" aria-label="More file actions" class="types__StyledButton-sc-ws60qy-0 ecnbuT js-blob-dropdown-click" title="More file actions" data-testid="more-file-actions-button-nav-menu-narrow" id=":R159badaj5:" aria-haspopup="true" tabindex="0" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button> </div></div></div></div><div id="StickyHeader" class="Box-sc-g0xbh4-0 bDwCYs react-code-view-header--wide"><div class="Box-sc-g0xbh4-0 fywjmm"><div class="Box-sc-g0xbh4-0 dyczTK"><div class="Box-sc-g0xbh4-0 kszRgZ"><div class="Box-sc-g0xbh4-0 eTvGbF"><nav data-testid="breadcrumbs" aria-labelledby="repos-header-breadcrumb-wide-heading" id="repos-header-breadcrumb-wide" class="Box-sc-g0xbh4-0 kzRgrI"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading" id="repos-header-breadcrumb-wide-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 cmAPIB"><li class="Box-sc-g0xbh4-0 jwXCBK"><a sx="[object Object]" data-testid="breadcrumbs-repo-link" class="Link__StyledLink-sc-14289xe-0 dpowyu" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/tree/main">encrypt-decrypt-pdf-file-with-AES256-</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 jwXCBK"><span aria-hidden="true" class="Text-sc-17v1xeu-0 ePvrxx">/</span><h1 tabindex="-1" id="file-name-id-wide" class="Heading__StyledHeading-sc-1c1dgg0-0 diwsLq">AES256.py</h1></div><button data-component="IconButton" type="button" aria-label="Copy path" data-testid="breadcrumb-copy-path-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 IIGly"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button></div></div><div class="Box-sc-g0xbh4-0 gtBUEp"><div class="d-flex gap-2"> <button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="l,Shift+L"></button><button hidden="" data-hotkey="l,Shift+L"></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Mod+Alt+g"></button><button hidden="" data-hotkey="Mod+Alt+g"></button><button type="button" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 bzquEC" data-hotkey="b,Shift+B,Control+/ Control+b"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text">Blame</span></span></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="b,Shift+B,Control+/ Control+b"></button><button data-component="IconButton" type="button" aria-label="More file actions" class="types__StyledButton-sc-ws60qy-0 ecnbuT js-blob-dropdown-click" title="More file actions" data-testid="more-file-actions-button-nav-menu-wide" id=":R176jadaj5:" aria-haspopup="true" tabindex="0" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button> </div></div></div></div></div></div></div><div class="Box-sc-g0xbh4-0 MERGN react-code-view-bottom-padding"> <div class="Box-sc-g0xbh4-0 cMYnca"></div><div class="Box-sc-g0xbh4-0"></div> <!-- --> <!-- --> </div><div class="Box-sc-g0xbh4-0 MERGN"> <!-- --> <!-- --> <button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="r,Shift+R"></button><button hidden="" data-hotkey="r,Shift+R"></button><div class="Box-sc-g0xbh4-0 dPsqPZ"><div class="Box-sc-g0xbh4-0 eYedVD"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading">Latest commit</h2><div data-testid="latest-commit" class="Box-sc-g0xbh4-0 drtGBr"><div class="Box-sc-g0xbh4-0 eScEiW"><div data-testid="author-avatar" class="Box-sc-g0xbh4-0 hLLhje"><a href="https://github.com/helmii18" data-testid="avatar-icon-link" data-hovercard-url="/users/helmii18/hovercard" class="Link__StyledLink-sc-14289xe-0 elltiT"><img alt="helmii18" size="20" src="./encrypt-decrypt-pdf-file-with-AES256-_AES256_files/106034331" data-testid="github-avatar" aria-label="helmii18" height="20" width="20" class="Avatar__StyledAvatar-sc-2lv0r8-0 gMUnCp"></a><span role="tooltip" aria-label="commits by helmii18" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-se"><a href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/commits?author=helmii18" aria-label="commits by helmii18" class="Link__StyledLink-sc-14289xe-0 fcwTtW">helmii18</a></span></div><span class="Box-sc-g0xbh4-0"></span></div><div class="Box-sc-g0xbh4-0 fqNQBl react-last-commit-message"><div class="Box-sc-g0xbh4-0 jEKUjt Truncate"><span class="Text-sc-17v1xeu-0 gPDEWA Truncate-text" data-testid="latest-commit-html"><a href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/commit/c3502d22160cddfe24145dcb3bd4a1c905e20137" class="Link--secondary" title="Update AES256.py" data-pjax="true" data-hovercard-url="/helmii18/encrypt-decrypt-pdf-file-with-AES256-/commit/c3502d22160cddfe24145dcb3bd4a1c905e20137/hovercard">Update AES256.py</a></span></div></div><span class="Text-sc-17v1xeu-0 gApqUp react-last-commit-summary-timestamp"><relative-time class="RelativeTime-sc-lqbqy3-0" datetime="2023-03-15T17:40:56.000+02:00" tense="past" title="Mar 15, 2023, 5:40 PM GMT+2"><template shadowrootmode="open">last year</template></relative-time></span></div><div class="Box-sc-g0xbh4-0 jGfYmh"><div data-testid="latest-commit-details" class="Box-sc-g0xbh4-0 lhFvfi"><span class="Text-sc-17v1xeu-0 gApqUp react-last-commit-oid-timestamp"><a class="Link__StyledLink-sc-14289xe-0 elltiT Link--secondary" aria-label="Commit c3502d2" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/commit/c3502d22160cddfe24145dcb3bd4a1c905e20137">c3502d2</a>&nbsp;·&nbsp;<relative-time class="RelativeTime-sc-lqbqy3-0" datetime="2023-03-15T17:40:56.000+02:00" tense="past" title="Mar 15, 2023, 5:40 PM GMT+2"><template shadowrootmode="open">last year</template></relative-time></span><span class="Text-sc-17v1xeu-0 gApqUp react-last-commit-timestamp"><relative-time class="RelativeTime-sc-lqbqy3-0" datetime="2023-03-15T17:40:56.000+02:00" tense="past" title="Mar 15, 2023, 5:40 PM GMT+2"><template shadowrootmode="open">last year</template></relative-time></span></div><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading">History</h2><a class="types__StyledButton-sc-ws60qy-0 saA-Dg react-last-commit-history-group" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/commits/main/AES256.py" data-size="small"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span><span data-component="text"><span class="Text-sc-17v1xeu-0 UrHoN">History</span></span></span></a><div class="Box-sc-g0xbh4-0 bqgLjk"><button data-component="IconButton" type="button" aria-label="Open commit details" aria-pressed="false" aria-expanded="false" data-testid="latest-commit-details-toggle" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 kiFJWH"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-ellipsis" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M0 5.75C0 4.784.784 4 1.75 4h12.5c.966 0 1.75.784 1.75 1.75v4.5A1.75 1.75 0 0 1 14.25 12H1.75A1.75 1.75 0 0 1 0 10.25ZM12 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2ZM7 8a1 1 0 1 0 2 0 1 1 0 0 0-2 0ZM4 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2Z"></path></svg></button></div><span role="tooltip" aria-label="Commit history" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a class="types__StyledButton-sc-ws60qy-0 saA-Dg react-last-commit-history-icon" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/commits/main/AES256.py"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span></span></a></span></div></div></div><div class="Box-sc-g0xbh4-0 iJmJly"><div class="Box-sc-g0xbh4-0 kjydbF container"><div class="Box-sc-g0xbh4-0 gIJuDf react-code-size-details-banner"><div class="Box-sc-g0xbh4-0 fleZSW react-code-size-details-banner"><div class="Box-sc-g0xbh4-0 dVVHlo text-mono"><div title="26.9 KB" data-testid="blob-size" class="Truncate__StyledTruncate-sc-23o1d2-0 fUpWeN"><span class="Text-sc-17v1xeu-0 gPDEWA">585 lines (518 loc) · 26.9 KB</span></div></div></div><div class="Box-sc-g0xbh4-0 react-code-size-details-banner"><button style="--button-color:fg.default" type="button" id=":R9faladaj5:" aria-haspopup="true" tabindex="0" data-testid="copilot-popover-button" data-size="small" class="types__StyledButton-sc-ws60qy-0 hhunph"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg></span><span data-component="text">Code 55% faster with GitHub Copilot</span></span></button></div></div><div class="Box-sc-g0xbh4-0 VHzRk react-blob-view-header-sticky" id="repos-sticky-header"><div class="Box-sc-g0xbh4-0 ePiodO"><div class="Box-sc-g0xbh4-0 react-blob-sticky-header"><div class="Box-sc-g0xbh4-0 kQJlnf"><div class="Box-sc-g0xbh4-0 gJICKO"><div class="Box-sc-g0xbh4-0 iZJewz"><nav data-testid="breadcrumbs" aria-labelledby="sticky-breadcrumb-heading" id="sticky-breadcrumb" class="Box-sc-g0xbh4-0 kzRgrI"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading" id="sticky-breadcrumb-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 cmAPIB"><li class="Box-sc-g0xbh4-0 jwXCBK"><a sx="[object Object]" data-testid="breadcrumbs-repo-link" class="Link__StyledLink-sc-14289xe-0 dpowyu" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/tree/main">encrypt-decrypt-pdf-file-with-AES256-</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 jwXCBK"><span aria-hidden="true" class="Text-sc-17v1xeu-0 fQxKLn">/</span><h1 tabindex="-1" id="sticky-file-name-id" class="Heading__StyledHeading-sc-1c1dgg0-0 jAEDJk">AES256.py</h1></div></div><button type="button" data-size="small" class="types__StyledButton-sc-ws60qy-0 ecGgfP" style="--button-color: fg.default;"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-arrow-up" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M3.47 7.78a.75.75 0 0 1 0-1.06l4.25-4.25a.75.75 0 0 1 1.06 0l4.25 4.25a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018L9 4.81v7.44a.75.75 0 0 1-1.5 0V4.81L4.53 7.78a.75.75 0 0 1-1.06 0Z"></path></svg></span><span data-component="text">Top</span></span></button></div></div></div><div class="Box-sc-g0xbh4-0 jtQniD"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading">File metadata and controls</h2><div class="Box-sc-g0xbh4-0 bfkNRF"><ul aria-label="File view" class="SegmentedControl__SegmentedControlList-sc-1rzig82-0 dlXtLG"><li class="Box-sc-g0xbh4-0 fXBLEV"><button aria-current="true" class="SegmentedControlButton__SegmentedControlButtonStyled-sc-8lkgxl-0 kNvrzW" data-hotkey="Control+/ Control+c"><span class="segmentedControl-content"><div class="Box-sc-g0xbh4-0 segmentedControl-text">Code</div></span></button></li><li class="Box-sc-g0xbh4-0 illvPQ"><button aria-current="false" class="SegmentedControlButton__SegmentedControlButtonStyled-sc-8lkgxl-0 iDBPxb" data-hotkey="b,Shift+B,Control+/ Control+b"><span class="segmentedControl-content"><div class="Box-sc-g0xbh4-0 segmentedControl-text">Blame</div></span></button></li></ul><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+/ Control+c"></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="b,Shift+B,Control+/ Control+b"></button><div class="Box-sc-g0xbh4-0 fleZSW react-code-size-details-in-header"><div class="Box-sc-g0xbh4-0 dVVHlo text-mono"><div title="26.9 KB" data-testid="blob-size" class="Truncate__StyledTruncate-sc-23o1d2-0 fUpWeN"><span class="Text-sc-17v1xeu-0 gPDEWA">585 lines (518 loc) · 26.9 KB</span></div></div></div><div class="Box-sc-g0xbh4-0 react-code-size-details-in-header"><button style="--button-color:fg.default" type="button" id=":Rt6faladaj5:" aria-haspopup="true" tabindex="0" data-testid="copilot-popover-button" data-size="small" class="types__StyledButton-sc-ws60qy-0 hhunph"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg></span><span data-component="text">Code 55% faster with GitHub Copilot</span></span></button></div></div><div class="Box-sc-g0xbh4-0 iBylDf"><button hidden="" data-testid="" data-hotkey="Control+Shift+&gt;" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Control+Shift+&gt;"></button><button hidden="" data-testid="" data-hotkey="Control+Shift+&lt;" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Control+Shift+&lt;"></button><div class="Box-sc-g0xbh4-0 kSGBPx react-blob-header-edit-and-raw-actions"><div class="ButtonGroup-sc-1gxhls1-0 cjbBGq"><a href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/raw/main/AES256.py" data-testid="raw-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 ctvgFa" data-hotkey="Control+/ Control+r"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text">Raw</span></span></a><button data-component="IconButton" type="button" aria-label="Copy raw content" data-testid="copy-raw-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 iqlNQz" data-hotkey="Control+Shift+C"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button><span role="tooltip" aria-label="Download raw file" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><button data-component="IconButton" type="button" aria-label="Download raw content" data-testid="download-raw-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 jKmxIb" data-hotkey="Control+Shift+S"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-download" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z"></path><path d="M7.25 7.689V2a.75.75 0 0 1 1.5 0v5.689l1.97-1.969a.749.749 0 1 1 1.06 1.06l-3.25 3.25a.749.749 0 0 1-1.06 0L4.22 6.78a.749.749 0 1 1 1.06-1.06l1.97 1.969Z"></path></svg></button></span></div><button hidden="" data-testid="raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+/ Control+r"></button><button hidden="" data-testid="copy-raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+Shift+C"></button><button hidden="" data-testid="download-raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+Shift+S"></button><a class="Link__StyledLink-sc-14289xe-0 elltiT js-github-dev-shortcut d-none" href="https://github.dev/" data-hotkey="., Control+Shift+/"></a><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="., Control+Shift+/"></button><a class="Link__StyledLink-sc-14289xe-0 elltiT js-github-dev-new-tab-shortcut d-none" href="https://github.dev/" target="_blank" data-hotkey="Shift+.,Shift+&gt;,&gt;"></a><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Shift+.,Shift+&gt;,&gt;"></button><div class="ButtonGroup-sc-1gxhls1-0 cjbBGq"><span role="tooltip" aria-label="Fork this repository and edit the file" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-nw"><a sx="[object Object]" data-component="IconButton" type="button" aria-label="Edit file" data-testid="edit-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 iwejsh" href="https://github.com/helmii18/encrypt-decrypt-pdf-file-with-AES256-/edit/main/AES256.py" data-hotkey="e,Shift+E"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-pencil" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg></a></span><button data-component="IconButton" type="button" aria-label="More edit options" data-testid="more-edit-button" id=":R2l76faladaj5:" aria-haspopup="true" tabindex="0" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 iqlNQz"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></button></div><button hidden="" data-testid="" data-hotkey="e,Shift+E" data-hotkey-scope="read-only-cursor-text-area"></button></div><span role="tooltip" aria-label="Close symbols panel" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-nw"><button data-component="IconButton" type="button" aria-label="Symbols" aria-pressed="true" aria-expanded="true" aria-controls="symbols-pane" class="types__StyledButton-sc-ws60qy-0 jgnIDP" data-testid="symbols-button" id="symbols-button" data-size="small" data-no-visuals="true" data-hotkey="Control+i"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-code-square" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25Zm7.47 3.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L10.69 8 9.22 6.53a.75.75 0 0 1 0-1.06ZM6.78 6.53 5.31 8l1.47 1.47a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path></svg></button></span><div class="Box-sc-g0xbh4-0 react-blob-header-edit-and-raw-actions-combined"><button data-component="IconButton" type="button" aria-label="Edit and raw actions" class="types__StyledButton-sc-ws60qy-0 htXhGX js-blob-dropdown-click" title="More file actions" data-testid="more-file-actions-button" id=":R5v6faladaj5:" aria-haspopup="true" tabindex="0" data-size="small" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button></div></div></div></div><div class="Box-sc-g0xbh4-0"></div></div><div class="Box-sc-g0xbh4-0 jMJFjm"><section aria-labelledby="file-name-id-wide file-name-id-mobile" class="Box-sc-g0xbh4-0 jWnGGx"><div class="Box-sc-g0xbh4-0 TCenl"><div id="highlighted-line-menu-positioner" class="position-relative"><div id="copilot-button-positioner" class="Box-sc-g0xbh4-0 cluMzC"><div class="Box-sc-g0xbh4-0 eRkHwF"><textarea id="read-only-cursor-text-area" aria-label="file content" aria-readonly="true" inputmode="none" tabindex="0" aria-multiline="true" aria-haspopup="false" data-gramm="false" data-gramm_editor="false" data-enable-grammarly="false" spellcheck="false" autocorrect="off" autocapitalize="off" autocomplete="off" data-ms-editor="false" class="react-blob-textarea react-blob-print-hide" style="resize: none; margin-top: -2px; padding-left: 92px; padding-right: 70px; width: 100%; background-color: unset; box-sizing: border-box; color: transparent; position: absolute; border: none; tab-size: 8; outline: none; overflow: auto hidden; height: 11700px; font-size: 12px; line-height: 20px; overflow-wrap: normal; overscroll-behavior-x: none; white-space: pre; z-index: 1;">import numpy as np
from base64 import b64encode, b64decode
import datetime
import base64

roundConstant = np.array([
    [0x01, 0x00, 0x00, 0x00],
    [0x02, 0x00, 0x00, 0x00],
    [0x04, 0x00, 0x00, 0x00],
    [0x08, 0x00, 0x00, 0x00],
    [0x10, 0x00, 0x00, 0x00],
    [0x20, 0x00, 0x00, 0x00],
    [0x40, 0x00, 0x00, 0x00],
    [0x80, 0x00, 0x00, 0x00],
    [0x1b, 0x00, 0x00, 0x00],
    [0x36, 0x00, 0x00, 0x00],
])

roundConstant_8 = np.array([
    [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x1b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x36, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
])


# Substitution Box: Encryption
s_box = np.array([
    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
    [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
    [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
    [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
    [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
    [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
    [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
    [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
    [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
    [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
    [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
    [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
    [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
    [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
    [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
    [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16],
])


# Substitution Box: Decryption
invs_box = np.array([
    [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
    [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
    [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
    [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
    [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
    [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
    [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
    [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
    [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
    [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
    [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
    [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
    [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
    [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
    [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
    [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d],
])


# Rijndael Galois Field: Encryption
encryptMDS = np.array([
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03, 0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02],
])


# Rijndael Galois Field: Encryption 8*8
encryptMDS_8 = np.array([
    [0x02, 0x01, 0x03, 0x01, 0x01, 0x01, 0x01, 0x01],
    [0x01, 0x03, 0x01, 0x01, 0x01, 0x01, 0x01, 0x02],
    [0x03, 0x01, 0x01, 0x01, 0x01, 0x01, 0x02, 0x01],
    [0x01, 0x01, 0x01, 0x01, 0x01, 0x02, 0x01, 0x03],
    [0x01, 0x01, 0x01, 0x01, 0x02, 0x01, 0x03, 0x01],
    [0x01, 0x01, 0x01, 0x02, 0x01, 0x03, 0x01, 0x01],
    [0x01, 0x01, 0x02, 0x01, 0x03, 0x01, 0x01, 0x01],
    [0x01, 0x02, 0x01, 0x03, 0x01, 0x01, 0x01, 0x01],
])


# Rijndael Galois Field: Decryption
decryptMDS = np.array([
    [0x0e, 0x0b, 0x0d, 0x09],
    [0x09, 0x0e, 0x0b, 0x0d],
    [0x0d, 0x09, 0x0e, 0x0b],
    [0x0b, 0x0d, 0x09, 0x0e],
])

# Rijndael Galois Field: Decryption 8*8
decryptMDS_8 = np.array([
    [0x0e, 0x01, 0x09, 0x01, 0x0d, 0x01, 0x0b, 0x01],
    [0x01, 0x09, 0x01, 0x0d, 0x01, 0x0b, 0x01, 0x0e],
    [0x09, 0x01, 0x0d, 0x01, 0x0b, 0x01, 0x0e, 0x01],
    [0x01, 0x0d, 0x01, 0x0b, 0x01, 0x0e, 0x01, 0x09],
    [0x0d, 0x01, 0x0b, 0x01, 0x0e, 0x01, 0x09, 0x01],
    [0x01, 0x0b, 0x01, 0x0e, 0x01, 0x09, 0x01, 0x0d],
    [0x0b, 0x01, 0x0e, 0x01, 0x09, 0x01, 0x0d, 0x01],
    [0x01, 0x0e, 0x01, 0x09, 0x01, 0x0d, 0x01, 0x0b],
])


# Look UP Table Mix Column:
mc2 = np.array([
    [0x00, 0x02, 0x04, 0x06, 0x08, 0x0a, 0x0c, 0x0e, 0x10, 0x12, 0x14, 0x16, 0x18, 0x1a, 0x1c, 0x1e],
    [0x20, 0x22, 0x24, 0x26, 0x28, 0x2a, 0x2c, 0x2e, 0x30, 0x32, 0x34, 0x36, 0x38, 0x3a, 0x3c, 0x3e],
    [0x40, 0x42, 0x44, 0x46, 0x48, 0x4a, 0x4c, 0x4e, 0x50, 0x52, 0x54, 0x56, 0x58, 0x5a, 0x5c, 0x5e],
    [0x60, 0x62, 0x64, 0x66, 0x68, 0x6a, 0x6c, 0x6e, 0x70, 0x72, 0x74, 0x76, 0x78, 0x7a, 0x7c, 0x7e],
    [0x80, 0x82, 0x84, 0x86, 0x88, 0x8a, 0x8c, 0x8e, 0x90, 0x92, 0x94, 0x96, 0x98, 0x9a, 0x9c, 0x9e],
    [0xa0, 0xa2, 0xa4, 0xa6, 0xa8, 0xaa, 0xac, 0xae, 0xb0, 0xb2, 0xb4, 0xb6, 0xb8, 0xba, 0xbc, 0xbe],
    [0xc0, 0xc2, 0xc4, 0xc6, 0xc8, 0xca, 0xcc, 0xce, 0xd0, 0xd2, 0xd4, 0xd6, 0xd8, 0xda, 0xdc, 0xde],
    [0xe0, 0xe2, 0xe4, 0xe6, 0xe8, 0xea, 0xec, 0xee, 0xf0, 0xf2, 0xf4, 0xf6, 0xf8, 0xfa, 0xfc, 0xfe],
    [0x1b, 0x19, 0x1f, 0x1d, 0x13, 0x11, 0x17, 0x15, 0x0b, 0x09, 0x0f, 0x0d, 0x03, 0x01, 0x07, 0x05],
    [0x3b, 0x39, 0x3f, 0x3d, 0x33, 0x31, 0x37, 0x35, 0x2b, 0x29, 0x2f, 0x2d, 0x23, 0x21, 0x27, 0x25],
    [0x5b, 0x59, 0x5f, 0x5d, 0x53, 0x51, 0x57, 0x55, 0x4b, 0x49, 0x4f, 0x4d, 0x43, 0x41, 0x47, 0x45],
    [0x7b, 0x79, 0x7f, 0x7d, 0x73, 0x71, 0x77, 0x75, 0x6b, 0x69, 0x6f, 0x6d, 0x63, 0x61, 0x67, 0x65],
    [0x9b, 0x99, 0x9f, 0x9d, 0x93, 0x91, 0x97, 0x95, 0x8b, 0x89, 0x8f, 0x8d, 0x83, 0x81, 0x87, 0x85],
    [0xbb, 0xb9, 0xbf, 0xbd, 0xb3, 0xb1, 0xb7, 0xb5, 0xab, 0xa9, 0xaf, 0xad, 0xa3, 0xa1, 0xa7, 0xa5],
    [0xdb, 0xd9, 0xdf, 0xdd, 0xd3, 0xd1, 0xd7, 0xd5, 0xcb, 0xc9, 0xcf, 0xcd, 0xc3, 0xc1, 0xc7, 0xc5],
    [0xfb, 0xf9, 0xff, 0xfd, 0xf3, 0xf1, 0xf7, 0xf5, 0xeb, 0xe9, 0xef, 0xed, 0xe3, 0xe1, 0xe7, 0xe5]
])


mc3 = np.array([
    [0x00, 0x03, 0x06, 0x05, 0x0c, 0x0f, 0x0a, 0x09, 0x18, 0x1b, 0x1e, 0x1d, 0x14, 0x17, 0x12, 0x11],
    [0x30, 0x33, 0x36, 0x35, 0x3c, 0x3f, 0x3a, 0x39, 0x28, 0x2b, 0x2e, 0x2d, 0x24, 0x27, 0x22, 0x21],
    [0x60, 0x63, 0x66, 0x65, 0x6c, 0x6f, 0x6a, 0x69, 0x78, 0x7b, 0x7e, 0x7d, 0x74, 0x77, 0x72, 0x71],
    [0x50, 0x53, 0x56, 0x55, 0x5c, 0x5f, 0x5a, 0x59, 0x48, 0x4b, 0x4e, 0x4d, 0x44, 0x47, 0x42, 0x41],
    [0xc0, 0xc3, 0xc6, 0xc5, 0xcc, 0xcf, 0xca, 0xc9, 0xd8, 0xdb, 0xde, 0xdd, 0xd4, 0xd7, 0xd2, 0xd1],
    [0xf0, 0xf3, 0xf6, 0xf5, 0xfc, 0xff, 0xfa, 0xf9, 0xe8, 0xeb, 0xee, 0xed, 0xe4, 0xe7, 0xe2, 0xe1],
    [0xa0, 0xa3, 0xa6, 0xa5, 0xac, 0xaf, 0xaa, 0xa9, 0xb8, 0xbb, 0xbe, 0xbd, 0xb4, 0xb7, 0xb2, 0xb1],
    [0x90, 0x93, 0x96, 0x95, 0x9c, 0x9f, 0x9a, 0x99, 0x88, 0x8b, 0x8e, 0x8d, 0x84, 0x87, 0x82, 0x81],
    [0x9b, 0x98, 0x9d, 0x9e, 0x97, 0x94, 0x91, 0x92, 0x83, 0x80, 0x85, 0x86, 0x8f, 0x8c, 0x89, 0x8a],
    [0xab, 0xa8, 0xad, 0xae, 0xa7, 0xa4, 0xa1, 0xa2, 0xb3, 0xb0, 0xb5, 0xb6, 0xbf, 0xbc, 0xb9, 0xba],
    [0xfb, 0xf8, 0xfd, 0xfe, 0xf7, 0xf4, 0xf1, 0xf2, 0xe3, 0xe0, 0xe5, 0xe6, 0xef, 0xec, 0xe9, 0xea],
    [0xcb, 0xc8, 0xcd, 0xce, 0xc7, 0xc4, 0xc1, 0xc2, 0xd3, 0xd0, 0xd5, 0xd6, 0xdf, 0xdc, 0xd9, 0xda],
    [0x5b, 0x58, 0x5d, 0x5e, 0x57, 0x54, 0x51, 0x52, 0x43, 0x40, 0x45, 0x46, 0x4f, 0x4c, 0x49, 0x4a],
    [0x6b, 0x68, 0x6d, 0x6e, 0x67, 0x64, 0x61, 0x62, 0x73, 0x70, 0x75, 0x76, 0x7f, 0x7c, 0x79, 0x7a],
    [0x3b, 0x38, 0x3d, 0x3e, 0x37, 0x34, 0x31, 0x32, 0x23, 0x20, 0x25, 0x26, 0x2f, 0x2c, 0x29, 0x2a],
    [0x0b, 0x08, 0x0d, 0x0e, 0x07, 0x04, 0x01, 0x02, 0x13, 0x10, 0x15, 0x16, 0x1f, 0x1c, 0x19, 0x1a]
])


mc9 = np.array([
    [0x00, 0x09, 0x12, 0x1b, 0x24, 0x2d, 0x36, 0x3f, 0x48, 0x41, 0x5a, 0x53, 0x6c, 0x65, 0x7e, 0x77],
    [0x90, 0x99, 0x82, 0x8b, 0xb4, 0xbd, 0xa6, 0xaf, 0xd8, 0xd1, 0xca, 0xc3, 0xfc, 0xf5, 0xee, 0xe7],
    [0x3b, 0x32, 0x29, 0x20, 0x1f, 0x16, 0x0d, 0x04, 0x73, 0x7a, 0x61, 0x68, 0x57, 0x5e, 0x45, 0x4c],
    [0xab, 0xa2, 0xb9, 0xb0, 0x8f, 0x86, 0x9d, 0x94, 0xe3, 0xea, 0xf1, 0xf8, 0xc7, 0xce, 0xd5, 0xdc],
    [0x76, 0x7f, 0x64, 0x6d, 0x52, 0x5b, 0x40, 0x49, 0x3e, 0x37, 0x2c, 0x25, 0x1a, 0x13, 0x08, 0x01],
    [0xe6, 0xef, 0xf4, 0xfd, 0xc2, 0xcb, 0xd0, 0xd9, 0xae, 0xa7, 0xbc, 0xb5, 0x8a, 0x83, 0x98, 0x91],
    [0x4d, 0x44, 0x5f, 0x56, 0x69, 0x60, 0x7b, 0x72, 0x05, 0x0c, 0x17, 0x1e, 0x21, 0x28, 0x33, 0x3a],
    [0xdd, 0xd4, 0xcf, 0xc6, 0xf9, 0xf0, 0xeb, 0xe2, 0x95, 0x9c, 0x87, 0x8e, 0xb1, 0xb8, 0xa3, 0xaa],
    [0xec, 0xe5, 0xfe, 0xf7, 0xc8, 0xc1, 0xda, 0xd3, 0xa4, 0xad, 0xb6, 0xbf, 0x80, 0x89, 0x92, 0x9b],
    [0x7c, 0x75, 0x6e, 0x67, 0x58, 0x51, 0x4a, 0x43, 0x34, 0x3d, 0x26, 0x2f, 0x10, 0x19, 0x02, 0x0b],
    [0xd7, 0xde, 0xc5, 0xcc, 0xf3, 0xfa, 0xe1, 0xe8, 0x9f, 0x96, 0x8d, 0x84, 0xbb, 0xb2, 0xa9, 0xa0],
    [0x47, 0x4e, 0x55, 0x5c, 0x63, 0x6a, 0x71, 0x78, 0x0f, 0x06, 0x1d, 0x14, 0x2b, 0x22, 0x39, 0x30],
    [0x9a, 0x93, 0x88, 0x81, 0xbe, 0xb7, 0xac, 0xa5, 0xd2, 0xdb, 0xc0, 0xc9, 0xf6, 0xff, 0xe4, 0xed],
    [0x0a, 0x03, 0x18, 0x11, 0x2e, 0x27, 0x3c, 0x35, 0x42, 0x4b, 0x50, 0x59, 0x66, 0x6f, 0x74, 0x7d],
    [0xa1, 0xa8, 0xb3, 0xba, 0x85, 0x8c, 0x97, 0x9e, 0xe9, 0xe0, 0xfb, 0xf2, 0xcd, 0xc4, 0xdf, 0xd6],
    [0x31, 0x38, 0x23, 0x2a, 0x15, 0x1c, 0x07, 0x0e, 0x79, 0x70, 0x6b, 0x62, 0x5d, 0x54, 0x4f, 0x46]
])

# 0x0b
mc11 = np.array([
    [0x00, 0x0b, 0x16, 0x1d, 0x2c, 0x27, 0x3a, 0x31, 0x58, 0x53, 0x4e, 0x45, 0x74, 0x7f, 0x62, 0x69],
    [0xb0, 0xbb, 0xa6, 0xad, 0x9c, 0x97, 0x8a, 0x81, 0xe8, 0xe3, 0xfe, 0xf5, 0xc4, 0xcf, 0xd2, 0xd9],
    [0x7b, 0x70, 0x6d, 0x66, 0x57, 0x5c, 0x41, 0x4a, 0x23, 0x28, 0x35, 0x3e, 0x0f, 0x04, 0x19, 0x12],
    [0xcb, 0xc0, 0xdd, 0xd6, 0xe7, 0xec, 0xf1, 0xfa, 0x93, 0x98, 0x85, 0x8e, 0xbf, 0xb4, 0xa9, 0xa2],
    [0xf6, 0xfd, 0xe0, 0xeb, 0xda, 0xd1, 0xcc, 0xc7, 0xae, 0xa5, 0xb8, 0xb3, 0x82, 0x89, 0x94, 0x9f],
    [0x46, 0x4d, 0x50, 0x5b, 0x6a, 0x61, 0x7c, 0x77, 0x1e, 0x15, 0x08, 0x03, 0x32, 0x39, 0x24, 0x2f],
    [0x8d, 0x86, 0x9b, 0x90, 0xa1, 0xaa, 0xb7, 0xbc, 0xd5, 0xde, 0xc3, 0xc8, 0xf9, 0xf2, 0xef, 0xe4],
    [0x3d, 0x36, 0x2b, 0x20, 0x11, 0x1a, 0x07, 0x0c, 0x65, 0x6e, 0x73, 0x78, 0x49, 0x42, 0x5f, 0x54],
    [0xf7, 0xfc, 0xe1, 0xea, 0xdb, 0xd0, 0xcd, 0xc6, 0xaf, 0xa4, 0xb9, 0xb2, 0x83, 0x88, 0x95, 0x9e],
    [0x47, 0x4c, 0x51, 0x5a, 0x6b, 0x60, 0x7d, 0x76, 0x1f, 0x14, 0x09, 0x02, 0x33, 0x38, 0x25, 0x2e],
    [0x8c, 0x87, 0x9a, 0x91, 0xa0, 0xab, 0xb6, 0xbd, 0xd4, 0xdf, 0xc2, 0xc9, 0xf8, 0xf3, 0xee, 0xe5],
    [0x3c, 0x37, 0x2a, 0x21, 0x10, 0x1b, 0x06, 0x0d, 0x64, 0x6f, 0x72, 0x79, 0x48, 0x43, 0x5e, 0x55],
    [0x01, 0x0a, 0x17, 0x1c, 0x2d, 0x26, 0x3b, 0x30, 0x59, 0x52, 0x4f, 0x44, 0x75, 0x7e, 0x63, 0x68],
    [0xb1, 0xba, 0xa7, 0xac, 0x9d, 0x96, 0x8b, 0x80, 0xe9, 0xe2, 0xff, 0xf4, 0xc5, 0xce, 0xd3, 0xd8],
    [0x7a, 0x71, 0x6c, 0x67, 0x56, 0x5d, 0x40, 0x4b, 0x22, 0x29, 0x34, 0x3f, 0x0e, 0x05, 0x18, 0x13],
    [0xca, 0xc1, 0xdc, 0xd7, 0xe6, 0xed, 0xf0, 0xfb, 0x92, 0x99, 0x84, 0x8f, 0xbe, 0xb5, 0xa8, 0xa3]
])


# 0x0d
mc13 = np.array([
    [0x00, 0x0d, 0x1a, 0x17, 0x34, 0x39, 0x2e, 0x23, 0x68, 0x65, 0x72, 0x7f, 0x5c, 0x51, 0x46, 0x4b],
    [0xd0, 0xdd, 0xca, 0xc7, 0xe4, 0xe9, 0xfe, 0xf3, 0xb8, 0xb5, 0xa2, 0xaf, 0x8c, 0x81, 0x96, 0x9b],
    [0xbb, 0xb6, 0xa1, 0xac, 0x8f, 0x82, 0x95, 0x98, 0xd3, 0xde, 0xc9, 0xc4, 0xe7, 0xea, 0xfd, 0xf0],
    [0x6b, 0x66, 0x71, 0x7c, 0x5f, 0x52, 0x45, 0x48, 0x03, 0x0e, 0x19, 0x14, 0x37, 0x3a, 0x2d, 0x20],
    [0x6d, 0x60, 0x77, 0x7a, 0x59, 0x54, 0x43, 0x4e, 0x05, 0x08, 0x1f, 0x12, 0x31, 0x3c, 0x2b, 0x26],
    [0xbd, 0xb0, 0xa7, 0xaa, 0x89, 0x84, 0x93, 0x9e, 0xd5, 0xd8, 0xcf, 0xc2, 0xe1, 0xec, 0xfb, 0xf6],
    [0xd6, 0xdb, 0xcc, 0xc1, 0xe2, 0xef, 0xf8, 0xf5, 0xbe, 0xb3, 0xa4, 0xa9, 0x8a, 0x87, 0x90, 0x9d],
    [0x06, 0x0b, 0x1c, 0x11, 0x32, 0x3f, 0x28, 0x25, 0x6e, 0x63, 0x74, 0x79, 0x5a, 0x57, 0x40, 0x4d],
    [0xda, 0xd7, 0xc0, 0xcd, 0xee, 0xe3, 0xf4, 0xf9, 0xb2, 0xbf, 0xa8, 0xa5, 0x86, 0x8b, 0x9c, 0x91],
    [0x0a, 0x07, 0x10, 0x1d, 0x3e, 0x33, 0x24, 0x29, 0x62, 0x6f, 0x78, 0x75, 0x56, 0x5b, 0x4c, 0x41],
    [0x61, 0x6c, 0x7b, 0x76, 0x55, 0x58, 0x4f, 0x42, 0x09, 0x04, 0x13, 0x1e, 0x3d, 0x30, 0x27, 0x2a],
    [0xb1, 0xbc, 0xab, 0xa6, 0x85, 0x88, 0x9f, 0x92, 0xd9, 0xd4, 0xc3, 0xce, 0xed, 0xe0, 0xf7, 0xfa],
    [0xb7, 0xba, 0xad, 0xa0, 0x83, 0x8e, 0x99, 0x94, 0xdf, 0xd2, 0xc5, 0xc8, 0xeb, 0xe6, 0xf1, 0xfc],
    [0x67, 0x6a, 0x7d, 0x70, 0x53, 0x5e, 0x49, 0x44, 0x0f, 0x02, 0x15, 0x18, 0x3b, 0x36, 0x21, 0x2c],
    [0x0c, 0x01, 0x16, 0x1b, 0x38, 0x35, 0x22, 0x2f, 0x64, 0x69, 0x7e, 0x73, 0x50, 0x5d, 0x4a, 0x47],
    [0xdc, 0xd1, 0xc6, 0xcb, 0xe8, 0xe5, 0xf2, 0xff, 0xb4, 0xb9, 0xae, 0xa3, 0x80, 0x8d, 0x9a, 0x97]
])


# 0x0e
mc14 = np.array([
    [0x00, 0x0e, 0x1c, 0x12, 0x38, 0x36, 0x24, 0x2a, 0x70, 0x7e, 0x6c, 0x62, 0x48, 0x46, 0x54, 0x5a],
    [0xe0, 0xee, 0xfc, 0xf2, 0xd8, 0xd6, 0xc4, 0xca, 0x90, 0x9e, 0x8c, 0x82, 0xa8, 0xa6, 0xb4, 0xba],
    [0xdb, 0xd5, 0xc7, 0xc9, 0xe3, 0xed, 0xff, 0xf1, 0xab, 0xa5, 0xb7, 0xb9, 0x93, 0x9d, 0x8f, 0x81],
    [0x3b, 0x35, 0x27, 0x29, 0x03, 0x0d, 0x1f, 0x11, 0x4b, 0x45, 0x57, 0x59, 0x73, 0x7d, 0x6f, 0x61],
    [0xad, 0xa3, 0xb1, 0xbf, 0x95, 0x9b, 0x89, 0x87, 0xdd, 0xd3, 0xc1, 0xcf, 0xe5, 0xeb, 0xf9, 0xf7],
    [0x4d, 0x43, 0x51, 0x5f, 0x75, 0x7b, 0x69, 0x67, 0x3d, 0x33, 0x21, 0x2f, 0x05, 0x0b, 0x19, 0x17],
    [0x76, 0x78, 0x6a, 0x64, 0x4e, 0x40, 0x52, 0x5c, 0x06, 0x08, 0x1a, 0x14, 0x3e, 0x30, 0x22, 0x2c],
    [0x96, 0x98, 0x8a, 0x84, 0xae, 0xa0, 0xb2, 0xbc, 0xe6, 0xe8, 0xfa, 0xf4, 0xde, 0xd0, 0xc2, 0xcc],
    [0x41, 0x4f, 0x5d, 0x53, 0x79, 0x77, 0x65, 0x6b, 0x31, 0x3f, 0x2d, 0x23, 0x09, 0x07, 0x15, 0x1b],
    [0xa1, 0xaf, 0xbd, 0xb3, 0x99, 0x97, 0x85, 0x8b, 0xd1, 0xdf, 0xcd, 0xc3, 0xe9, 0xe7, 0xf5, 0xfb],
    [0x9a, 0x94, 0x86, 0x88, 0xa2, 0xac, 0xbe, 0xb0, 0xea, 0xe4, 0xf6, 0xf8, 0xd2, 0xdc, 0xce, 0xc0],
    [0x7a, 0x74, 0x66, 0x68, 0x42, 0x4c, 0x5e, 0x50, 0x0a, 0x04, 0x16, 0x18, 0x32, 0x3c, 0x2e, 0x20],
    [0xec, 0xe2, 0xf0, 0xfe, 0xd4, 0xda, 0xc8, 0xc6, 0x9c, 0x92, 0x80, 0x8e, 0xa4, 0xaa, 0xb8, 0xb6],
    [0x0c, 0x02, 0x10, 0x1e, 0x34, 0x3a, 0x28, 0x26, 0x7c, 0x72, 0x60, 0x6e, 0x44, 0x4a, 0x58, 0x56],
    [0x37, 0x39, 0x2b, 0x25, 0x0f, 0x01, 0x13, 0x1d, 0x47, 0x49, 0x5b, 0x55, 0x7f, 0x71, 0x63, 0x6d],
    [0xd7, 0xd9, 0xcb, 0xc5, 0xef, 0xe1, 0xf3, 0xfd, 0xa7, 0xa9, 0xbb, 0xb5, 0x9f, 0x91, 0x83, 0x8d]
])



# Key to Matrix
def keyToHexArray(key, row=4, col=4):
    arr = []
    for i in key:
        arr.append(ord(i))
    arr = np.array(arr)
    arr = arr.reshape(row, col)  # 4*4 matrix
    return arr


# Apply left shift / RotWord
def arrayShift(arr, shift=-1):
    return np.roll(arr, shift)


# S-box on 1D Array
def arraySbox(arr):
    for i in range(0, len(arr)):
        lsb = arr[i] &amp; 0b00001111
        msb = (arr[i] &amp; 0b11110000) &gt;&gt; 4
        arr[i] = s_box[msb, lsb]
    return arr


# Inverse S-box on 1D Array
def arrayInvSbox(arr):
    for i in range(0, len(arr)):
        lsb = arr[i] &amp; 0b00001111
        msb = (arr[i] &amp; 0b11110000) &gt;&gt; 4
        arr[i] = invs_box[msb, lsb]
    return arr


# XOR Operation on [arr1, arr2] or [arr1,arr2,rcon(i)]
def xorArray(arr1, arr2, order=4, rcon=-1):
    xor_arr = []
    if (arr1.shape == arr2.shape and (rcon &gt;= -1 and rcon &lt;= 9)):
        if (rcon == -1):
            for i in range(len(arr1)):
                val = arr1[i] ^ arr2[i]
                xor_arr.append(val)
        else:
            rcon_arr = roundConstant[rcon]
            if (order == 8):
                rcon_arr = roundConstant_8[rcon]
            for i in range(len(arr1)):
                val = arr1[i] ^ arr2[i] ^ rcon_arr[i]
                xor_arr.append(val)
        xor_arr = np.array(xor_arr)
        return xor_arr
    else:
        print('Array must be same dimension numpy OR Rcon: roundconstant must be 0-10')
        print(arr1, arr2, rcon)
        return False


# Xor 2 2D array
def addRoundKey(arr1, arr2):
    return np.bitwise_xor(arr1, arr2)


# Substitution-box on 2D Array
def subBytes(arr, inverse=False):
    for i in arr:
        if (not inverse):
            arraySbox(i)
        else:
            arrayInvSbox(i)
    return arr


# Shift Row on 2D Array
def shiftRow(arr, left=True, order=4):
    shifted_arr = []
    for i in range(0, order):
        if (left):
            x = arrayShift(arr[:, i], -1 * i)  # Left circular shift: Encryption
        else:
            x = arrayShift(arr[:, i], i)  # Right circular shift: Decryption
        shifted_arr.append(x)
    shifted_arr = np.array(shifted_arr)  # Accurate
    return np.transpose(shifted_arr)


# Mix Column
def mixColumn(arr, order=4):
    arr = np.transpose(arr)
    mix_arr = np.zeros((order, order), dtype=int)
    encryptMDS_arr = encryptMDS
    if (order == 8):
        encryptMDS_arr = encryptMDS_8
    for i in range(0, order):
        for j in range(0, order):
            for k in range(0, order):
                if (encryptMDS_arr[i][k] == 1):
                    mix_arr[i][j] ^= arr[k][j]
                lsb = arr[k][j] &amp; 0b00001111
                msb = (arr[k][j] &amp; 0b11110000) &gt;&gt; 4
                if (encryptMDS_arr[i][k] == 2):
                    mix_arr[i][j] ^= mc2[msb, lsb]
                if (encryptMDS_arr[i][k] == 3):
                    mix_arr[i][j] ^= mc3[msb, lsb]
    return np.transpose(mix_arr)


# Inverse Mix Column
def inverseMixColumn(arr, order=4):
    decryptMDS_arr = decryptMDS
    if (order == 8):
        decryptMDS_arr = decryptMDS_8
    arr = np.transpose(arr)
    mix_arr = np.zeros((order, order), dtype=int)
    for i in range(0, order):
        for j in range(0, order):
            for k in range(0, order):
                if (decryptMDS_arr[i][k] == 1):
                    mix_arr[i][j] ^= arr[k][j]
                lsb = arr[k][j] &amp; 0b00001111
                msb = (arr[k][j] &amp; 0b11110000) &gt;&gt; 4
                if (decryptMDS_arr[i][k] == 9):
                    mix_arr[i][j] ^= mc9[msb, lsb]
                if (decryptMDS_arr[i][k] == 11):
                    mix_arr[i][j] ^= mc11[msb, lsb]
                if (decryptMDS_arr[i][k] == 13):
                    mix_arr[i][j] ^= mc13[msb, lsb]
                if (decryptMDS_arr[i][k] == 14):
                    mix_arr[i][j] ^= mc14[msb, lsb]
    return np.transpose(mix_arr)


# Decryption: ecrypted hex to matrix
'''
4*4: 16 box =&gt; 128 bits =&gt; 32 in hex (representation)
8*8: 64 box =&gt; 512 bits =&gt; 128 in hex (representation)
'''


def hexToMatrix(data, order=4):
    hexbit = order * order * 2
    if (len(data) == hexbit):
        val = [data[i:i + 2] for i in range(0, len(data), 2)]
        val = [int(x, 16) for x in val]
        arr = np.array(val)
        arr = arr.reshape(order, order)  # 4*4 matrix
        return arr
    else:
        print('length of encrypted data should be 32')

class AES:

    def __init__(self):
        self.ROUND = 14
        self.ROUNDKEY = []

    # Key Scheduling
    def __keySchedule(self, KEY):
        ROW, COL = 8, 4
        EXPANSION = 7
        hexKey = keyToHexArray(KEY, ROW, COL)
        self.ROUNDKEY.append(hexKey)
        for i in range(0, EXPANSION):
            prev_arr = self.ROUNDKEY[-1]
            last_col = prev_arr[ROW - 1]
            shift_col = arrayShift(last_col)
            sbox_col = arraySbox(shift_col)
            col_1 = xorArray(prev_arr[0], sbox_col, i)
            col_2 = xorArray(col_1, prev_arr[1])
            col_3 = xorArray(col_2, prev_arr[2])
            col_4 = xorArray(col_3, prev_arr[3])
            # additional non-linear transformation after the fourth column
            col_5 = xorArray(arraySbox(np.copy(col_4)), prev_arr[4])
            col_6 = xorArray(col_5, prev_arr[5])
            col_7 = xorArray(col_6, prev_arr[6])
            col_8 = xorArray(col_7, prev_arr[7])
            new_arr = np.array([col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8])
            self.ROUNDKEY.append(new_arr)
        self.__convertRoundKey()

    # Convert 8 4*8 Matrix to 15 4*4 Matrix
    def __convertRoundKey(self):
        self.ROUNDKEY = np.concatenate(self.ROUNDKEY)
        temp = []
        for i in range(self.ROUND + 1):
            temp.append(self.ROUNDKEY[i * 4:i * 4 + 4])
        self.ROUNDKEY = temp

    # Encryption Process
    def __encryptProcess(self, TEXT):
        print(TEXT)
        hexData = keyToHexArray(TEXT)
        print("after convert to hexdata" , hexData)
        cipher_arr = addRoundKey(hexData, self.ROUNDKEY[0])
        print("cipher arr ",cipher_arr)
        for i in range(1, self.ROUND + 1):
            print("\nround " ,i,"\n")
            arr = cipher_arr
            print("cipher arr ", arr)
            arr = subBytes(arr)
            print("after sub bytes",arr)
            arr = shiftRow(arr)
            print("after shift rows",arr)
            if (i != self.ROUND):
                arr = mixColumn(arr)
                # print("after mix columns",arr)
            arr = addRoundKey(arr, self.ROUNDKEY[i])
            cipher_arr = arr
        return cipher_arr

    # Encryption Add Padding
    def __addPadding(self, data):
        bytes = 16
        bits_arr = []
        while (True):
            if (len(data) &gt; bytes):
                bits_arr.append(data[:bytes])
                data = data[bytes:]
            else:
                space = bytes - len(data)
                bits_arr.append(data + chr(space) * space)
                break
        return bits_arr

    # Decryption Process
    def __decryptProcess(self, CIPHER_HEX):
        hexData = hexToMatrix(CIPHER_HEX)
        plain_arr = addRoundKey(hexData, self.ROUNDKEY[-1])
        for i in range(self.ROUND - 1, -1, -1):
            print("\nround ", i, "\n")
            arr = plain_arr
            print("plain arr ", arr)
            arr = shiftRow(arr, left=False)
            print("after inverse of shift rows", arr)
            arr = subBytes(arr, inverse=True)
            print("after inverse of sub bytes", arr)
            arr = addRoundKey(arr, self.ROUNDKEY[i])
            if (i != 0):
                arr = inverseMixColumn(arr)
                print("after inverse mix columns", arr)
            plain_arr = arr
        return plain_arr

    # Decryption Delete Padding
    def __delPadding(self, data):
        verify = data[-1]
        bytes = 16
        if (verify &gt;= 1 and verify &lt;= bytes - 1):
            pad = data[bytes - verify:]
            sameCount = pad.count(verify)
            if (sameCount == verify):
                return data[:bytes - verify]
            return data
        return data

    # Encryption
    def encrypt(self, KEY, TEXT, type='hex'):
        text_arr = self.__addPadding(TEXT)
        print("after add padding",text_arr)
        self.__keySchedule(KEY)
        hex_ecrypt = ''
        for i in text_arr:
            cipher_matrix = self.__encryptProcess(i)
            cipher_text = list(np.array(cipher_matrix).reshape(-1, ))
            for j in cipher_text:
                hex_ecrypt += f'{j:02x}'
        self.ROUNDKEY = []
        # conversion
        if (type == 'b64'):
            return b64encode(bytes.fromhex(hex_ecrypt)).decode()
        if (type == '0b'):
            return f'{int(hex_ecrypt, 16):0&gt;b}'
        if (type == '__all__'):
            return {
                'hex': hex_ecrypt,
                'b64': b64encode(bytes.fromhex(hex_ecrypt)).decode(),
                '0b': bin(int(hex_ecrypt, 16))[2:].zfill(len(hex_ecrypt) * 4)
            }
        return hex_ecrypt

    # Decryption
    def decrypt(self, KEY, CIPHER, type='hex'):
        if type in ['hex', '0b', 'b64']:
            self.__keySchedule(KEY)
            data = ''

            if (type == 'b64'):
                CIPHER = b64decode(CIPHER).hex()
                print("cipher in b64",CIPHER)
            if (type == '0b'):
                CIPHER = hex(int(CIPHER, 2)).replace('0x', '')
                print("cipher in 0b",CIPHER)
            if (len(CIPHER) % 32 == 0 and len(CIPHER) &gt; 0):
                examine = CIPHER
                while (len(examine) != 0):
                    plain_matrix = self.__decryptProcess(examine[:32])
                    plain_arr = list(np.array(plain_matrix).reshape(-1, ))
                    plain_arr = self.__delPadding(plain_arr)
                    for j in plain_arr:
                        data += chr(j)
                    if (len(examine) == 32):
                        examine = ''
                    else:
                        examine = examine[32:]
                self.ROUNDKEY = []
                return data

            else:
                raise Exception(f"Hex: {CIPHER}, should be non-empty multiple of 32bits")

        else:
            raise Exception(f"type := ['hex', '0b', 'b64'] but got '{type}'")


if (__name__ == '__main__'):
    aes256 = AES()
    key = 'Thats my Kung Fu1234567876543210'
    print("***************************************")
    filenameencypt=input("enter file name to encryption ")+".pdf"

    with open(filenameencypt, "rb") as pdf_file:
        encoded = base64.b64encode(pdf_file.read())
        encoded_string=encoded.decode('utf-8')
    stretime = datetime.datetime.now()
    c=(aes256.encrypt(key,encoded_string,'0b'))
    endetime = datetime.datetime.now()
    print("encryption takes ", (endetime - stretime).microseconds * 1000, " milli seconds")
    file_64_decodee10 = base64.b64decode(c)
    file_resultc = open('encryption file.pdf', 'wb')
    file_resultc.write(file_64_decodee10)
    print("encryption done with encryption file")

    print("***************************************")
    filenamedecrypt=input("enter file to decryption")+".pdf"
    with open(filenamedecrypt, "rb") as pdf_file:
        cc = base64.b64encode(pdf_file.read())
    strtimdec = datetime.datetime.now()
    m=aes256.decrypt(key,cc,'0b')
    endetimdec = datetime.datetime.now()
    print("encryption takes ", (endetimdec- strtimdec).microseconds * 1000, " milli seconds")
    file_64_decoded00 = base64.b64decode(m)
    file_result00 = open('decryption file.pdf', 'wb')
    file_result00.write(file_64_decoded00)
    print("***************************************")
    print("decryption done with decryption file")</textarea><button hidden="" data-testid="" data-hotkey="Alt+F1,Control+Alt+˙,Control+Alt+h" data-hotkey-scope="read-only-cursor-text-area"></button><div class="Box-sc-g0xbh4-0 cXpbTk"><div tabindex="0" class="Box-sc-g0xbh4-0 hHjsH"><div class="Box-sc-g0xbh4-0 VkLKX react-code-file-contents" role="presentation" aria-hidden="true" data-tab-size="8" data-paste-markdown-skip="true" data-hpc="true" style="height: 11680px;"><div class="react-line-numbers" style="pointer-events: auto; height: 11680px; position: relative; z-index: 2;"><div data-line-number="1" class="react-line-number react-code-text" style="padding-right: 16px;">1</div><div data-line-number="2" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(20px);">2</div><div data-line-number="3" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(40px);">3</div><div data-line-number="4" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(60px);">4</div><div data-line-number="5" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(80px);">5</div><div data-line-number="6" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(100px);">6<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="7" class="child-of-line-6  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(120px);">7</div><div data-line-number="8" class="child-of-line-6  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(140px);">8</div><div data-line-number="9" class="child-of-line-6  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(160px);">9</div><div data-line-number="10" class="child-of-line-6  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(180px);">10</div><div data-line-number="11" class="child-of-line-6  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(200px);">11</div><div data-line-number="12" class="child-of-line-6  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(220px);">12</div><div data-line-number="13" class="child-of-line-6  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(240px);">13</div><div data-line-number="14" class="child-of-line-6  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(260px);">14</div><div data-line-number="15" class="child-of-line-6  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(280px);">15</div><div data-line-number="16" class="child-of-line-6  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(300px);">16</div><div data-line-number="17" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(320px);">17</div><div data-line-number="18" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(340px);">18</div><div data-line-number="19" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(360px);">19<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="20" class="child-of-line-19  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(380px);">20</div><div data-line-number="21" class="child-of-line-19  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(400px);">21</div><div data-line-number="22" class="child-of-line-19  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(420px);">22</div><div data-line-number="23" class="child-of-line-19  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(440px);">23</div><div data-line-number="24" class="child-of-line-19  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(460px);">24</div><div data-line-number="25" class="child-of-line-19  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(480px);">25</div><div data-line-number="26" class="child-of-line-19  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(500px);">26</div><div data-line-number="27" class="child-of-line-19  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(520px);">27</div><div data-line-number="28" class="child-of-line-19  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(540px);">28</div><div data-line-number="29" class="child-of-line-19  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(560px);">29</div><div data-line-number="30" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(580px);">30</div><div data-line-number="31" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(600px);">31</div><div data-line-number="32" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(620px);">32</div><div data-line-number="33" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(640px);">33</div><div data-line-number="34" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(660px);">34<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="35" class="child-of-line-34  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(680px);">35</div><div data-line-number="36" class="child-of-line-34  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(700px);">36</div><div data-line-number="37" class="child-of-line-34  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(720px);">37</div><div data-line-number="38" class="child-of-line-34  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(740px);">38</div><div data-line-number="39" class="child-of-line-34  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(760px);">39</div><div data-line-number="40" class="child-of-line-34  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(780px);">40</div><div data-line-number="41" class="child-of-line-34  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(800px);">41</div><div data-line-number="42" class="child-of-line-34  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(820px);">42</div><div data-line-number="43" class="child-of-line-34  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(840px);">43</div><div data-line-number="44" class="child-of-line-34  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(860px);">44</div><div data-line-number="45" class="child-of-line-34  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(880px);">45</div><div data-line-number="46" class="child-of-line-34  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(900px);">46</div><div data-line-number="47" class="child-of-line-34  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(920px);">47</div><div data-line-number="48" class="child-of-line-34  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(940px);">48</div><div data-line-number="49" class="child-of-line-34  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(960px);">49</div><div data-line-number="50" class="child-of-line-34  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(980px);">50</div><div data-line-number="51" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1000px);">51</div><div data-line-number="52" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1020px);">52</div><div data-line-number="53" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1040px);">53</div><div data-line-number="54" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1060px);">54</div><div data-line-number="55" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1080px);">55<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="56" class="child-of-line-55  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1100px);">56</div><div data-line-number="57" class="child-of-line-55  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1120px);">57</div><div data-line-number="58" class="child-of-line-55  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1140px);">58</div><div data-line-number="59" class="child-of-line-55  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1160px);">59</div><div data-line-number="60" class="child-of-line-55  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1180px);">60</div><div data-line-number="61" class="child-of-line-55  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1200px);">61</div><div data-line-number="62" class="child-of-line-55  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1220px);">62</div><div data-line-number="63" class="child-of-line-55  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1240px);">63</div><div data-line-number="64" class="child-of-line-55  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1260px);">64</div><div data-line-number="65" class="child-of-line-55  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1280px);">65</div><div data-line-number="66" class="child-of-line-55  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1300px);">66</div><div data-line-number="67" class="child-of-line-55  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1320px);">67</div><div data-line-number="68" class="child-of-line-55  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1340px);">68</div><div data-line-number="69" class="child-of-line-55  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1360px);">69</div><div data-line-number="70" class="child-of-line-55  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1380px);">70</div><div data-line-number="71" class="child-of-line-55  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1400px);">71</div><div data-line-number="72" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1420px);">72</div><div data-line-number="73" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1440px);">73</div><div data-line-number="74" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1460px);">74</div><div data-line-number="75" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1480px);">75</div><div data-line-number="76" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1500px);">76<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="77" class="child-of-line-76  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1520px);">77</div><div data-line-number="78" class="child-of-line-76  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1540px);">78</div><div data-line-number="79" class="child-of-line-76  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1560px);">79</div><div data-line-number="80" class="child-of-line-76  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1580px);">80</div><div data-line-number="81" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1600px);">81</div><div data-line-number="82" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1620px);">82</div><div data-line-number="83" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1640px);">83</div><div data-line-number="84" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1660px);">84</div><div data-line-number="85" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1680px);">85<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="86" class="child-of-line-85  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1700px);">86</div><div data-line-number="87" class="child-of-line-85  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1720px);">87</div><div data-line-number="88" class="child-of-line-85  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1740px);">88</div><div data-line-number="89" class="child-of-line-85  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1760px);">89</div><div data-line-number="90" class="child-of-line-85  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1780px);">90</div><div data-line-number="91" class="child-of-line-85  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1800px);">91</div><div data-line-number="92" class="child-of-line-85  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1820px);">92</div><div data-line-number="93" class="child-of-line-85  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1840px);">93</div><div data-line-number="94" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1860px);">94</div><div data-line-number="95" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1880px);">95</div><div data-line-number="96" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1900px);">96</div><div data-line-number="97" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1920px);">97</div><div data-line-number="98" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1940px);">98<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="99" class="child-of-line-98  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1960px);">99</div><div data-line-number="100" class="child-of-line-98  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1980px);">100</div><div data-line-number="101" class="child-of-line-98  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2000px);">101</div><div data-line-number="102" class="child-of-line-98  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2020px);">102</div><div data-line-number="103" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2040px);">103</div><div data-line-number="104" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2060px);">104</div><div data-line-number="105" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2080px);">105</div><div data-line-number="106" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2100px);">106<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="107" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2120px);">107</div><div data-line-number="108" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2140px);">108</div><div data-line-number="109" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2160px);">109</div><div data-line-number="110" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2180px);">110</div><div data-line-number="111" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2200px);">111</div><div data-line-number="112" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2220px);">112</div><div data-line-number="113" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2240px);">113</div><div data-line-number="114" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2260px);">114</div><div data-line-number="115" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2280px);">115</div><div data-line-number="116" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2300px);">116</div><div data-line-number="117" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2320px);">117</div><div data-line-number="118" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2340px);">118</div><div data-line-number="119" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2360px);">119<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="120" class="child-of-line-119  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2380px);">120</div><div data-line-number="121" class="child-of-line-119  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2400px);">121</div><div data-line-number="122" class="child-of-line-119  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2420px);">122</div><div data-line-number="123" class="child-of-line-119  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2440px);">123</div><div data-line-number="511" class="child-of-line-390 child-of-line-496  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10200px);">511</div><div data-line-number="512" class="child-of-line-390 child-of-line-496  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10220px);">512</div><div data-line-number="513" class="child-of-line-390 child-of-line-496  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10240px);">513</div><div data-line-number="514" class="child-of-line-390 child-of-line-496  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10260px);">514</div><div data-line-number="515" class="child-of-line-390 child-of-line-496  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10280px);">515</div><div data-line-number="516" class="child-of-line-390 child-of-line-496  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10300px);">516</div><div data-line-number="517" class="child-of-line-390 child-of-line-496  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10320px);">517</div><div data-line-number="518" class="child-of-line-390  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10340px);">518</div><div data-line-number="519" class="child-of-line-390  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10360px);">519</div><div data-line-number="520" class="child-of-line-390  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10380px);">520</div><div data-line-number="521" class="child-of-line-390  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10400px);">521<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="522" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10420px);">522</div><div data-line-number="523" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10440px);">523</div><div data-line-number="524" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10460px);">524</div><div data-line-number="525" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10480px);">525</div><div data-line-number="526" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10500px);">526</div><div data-line-number="527" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10520px);">527</div><div data-line-number="528" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10540px);">528</div><div data-line-number="529" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10560px);">529</div><div data-line-number="530" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10580px);">530</div><div data-line-number="531" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10600px);">531</div><div data-line-number="532" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10620px);">532</div><div data-line-number="533" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10640px);">533</div><div data-line-number="534" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10660px);">534</div><div data-line-number="535" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10680px);">535</div><div data-line-number="536" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10700px);">536</div><div data-line-number="537" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10720px);">537</div><div data-line-number="538" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10740px);">538</div><div data-line-number="539" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10760px);">539</div><div data-line-number="540" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10780px);">540</div><div data-line-number="541" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10800px);">541</div><div data-line-number="542" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10820px);">542</div><div data-line-number="543" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10840px);">543</div><div data-line-number="544" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10860px);">544</div><div data-line-number="545" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10880px);">545</div><div data-line-number="546" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10900px);">546</div><div data-line-number="547" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10920px);">547</div><div data-line-number="548" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10940px);">548</div><div data-line-number="549" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10960px);">549</div><div data-line-number="550" class="child-of-line-390 child-of-line-521  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(10980px);">550</div><div data-line-number="551" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11000px);">551</div><div data-line-number="552" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11020px);">552</div><div data-line-number="553" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11040px);">553</div><div data-line-number="554" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11060px);">554</div><div data-line-number="555" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11080px);">555</div><div data-line-number="556" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11100px);">556</div><div data-line-number="557" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11120px);">557</div><div data-line-number="558" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11140px);">558</div><div data-line-number="559" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11160px);">559</div><div data-line-number="560" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11180px);">560</div><div data-line-number="561" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11200px);">561</div><div data-line-number="562" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11220px);">562</div><div data-line-number="563" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11240px);">563</div><div data-line-number="564" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11260px);">564</div><div data-line-number="565" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11280px);">565</div><div data-line-number="566" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11300px);">566</div><div data-line-number="567" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11320px);">567</div><div data-line-number="568" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11340px);">568</div><div data-line-number="569" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11360px);">569</div><div data-line-number="570" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11380px);">570</div><div data-line-number="571" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11400px);">571</div><div data-line-number="572" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11420px);">572</div><div data-line-number="573" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11440px);">573</div><div data-line-number="574" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11460px);">574</div><div data-line-number="575" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11480px);">575</div><div data-line-number="576" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11500px);">576</div><div data-line-number="577" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11520px);">577</div><div data-line-number="578" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11540px);">578</div><div data-line-number="579" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11560px);">579</div><div data-line-number="580" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11580px);">580</div><div data-line-number="581" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11600px);">581</div><div data-line-number="582" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11620px);">582</div><div data-line-number="583" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11640px);">583</div><div data-line-number="584" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(11660px);">584</div></div><div class="react-code-lines" style="height: 11680px;"><div data-key="0" class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC1" class="react-file-line html-div" data-testid="code-cell" data-line-number="1" style="position: relative;"><span class="pl-k" data-code-text="import"></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="numpy"></span><span data-code-text=" "></span><span class="pl-k" data-code-text="as"></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="np"></span></div></div></div><div data-key="1" class="react-code-text react-code-line-contents virtual" style="transform: translateY(20px); min-height: auto;"><div><div id="LC2" class="react-file-line html-div" data-testid="code-cell" data-line-number="2" style="position: relative;"><span class="pl-k" data-code-text="from"></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="base64"></span><span data-code-text=" "></span><span class="pl-k" data-code-text="import"></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="b64encode"></span><span data-code-text=", "></span><span class="pl-s1" data-code-text="b64decode"></span></div></div></div><div data-key="2" class="react-code-text react-code-line-contents virtual" style="transform: translateY(40px); min-height: auto;"><div><div id="LC3" class="react-file-line html-div" data-testid="code-cell" data-line-number="3" style="position: relative;"><span class="pl-k" data-code-text="import"></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="datetime"></span></div></div></div><div data-key="3" class="react-code-text react-code-line-contents virtual" style="transform: translateY(60px); min-height: auto;"><div><div id="LC4" class="react-file-line html-div" data-testid="code-cell" data-line-number="4" style="position: relative;"><span class="pl-k" data-code-text="import"></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="base64"></span></div></div></div><div data-key="4" class="react-code-text react-code-line-contents virtual" style="transform: translateY(80px); min-height: auto;"><div><div id="LC5" class="react-file-line html-div" data-testid="code-cell" data-line-number="5" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="5" class="react-code-text react-code-line-contents virtual" style="transform: translateY(100px); min-height: auto;"><div><div id="LC6" class="react-file-line html-div" data-testid="code-cell" data-line-number="6" style="position: relative;"><span class="pl-s1" data-code-text="roundConstant"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="np"></span><span data-code-text="."></span><span class="pl-en" data-code-text="array"></span><span data-code-text="(["></span></div></div></div><div data-key="6" class="child-of-line-6  react-code-text react-code-line-contents virtual" style="transform: translateY(120px); min-height: auto;"><div><div id="LC7" class="react-file-line html-div" data-testid="code-cell" data-line-number="7" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text="],"></span></div></div></div><div data-key="7" class="child-of-line-6  react-code-text react-code-line-contents virtual" style="transform: translateY(140px); min-height: auto;"><div><div id="LC8" class="react-file-line html-div" data-testid="code-cell" data-line-number="8" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x02"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text="],"></span></div></div></div><div data-key="8" class="child-of-line-6  react-code-text react-code-line-contents virtual" style="transform: translateY(160px); min-height: auto;"><div><div id="LC9" class="react-file-line html-div" data-testid="code-cell" data-line-number="9" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x04"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text="],"></span></div></div></div><div data-key="9" class="child-of-line-6  react-code-text react-code-line-contents virtual" style="transform: translateY(180px); min-height: auto;"><div><div id="LC10" class="react-file-line html-div" data-testid="code-cell" data-line-number="10" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x08"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text="],"></span></div></div></div><div data-key="10" class="child-of-line-6  react-code-text react-code-line-contents virtual" style="transform: translateY(200px); min-height: auto;"><div><div id="LC11" class="react-file-line html-div" data-testid="code-cell" data-line-number="11" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x10"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text="],"></span></div></div></div><div data-key="11" class="child-of-line-6  react-code-text react-code-line-contents virtual" style="transform: translateY(220px); min-height: auto;"><div><div id="LC12" class="react-file-line html-div" data-testid="code-cell" data-line-number="12" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x20"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text="],"></span></div></div></div><div data-key="12" class="child-of-line-6  react-code-text react-code-line-contents virtual" style="transform: translateY(240px); min-height: auto;"><div><div id="LC13" class="react-file-line html-div" data-testid="code-cell" data-line-number="13" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x40"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text="],"></span></div></div></div><div data-key="13" class="child-of-line-6  react-code-text react-code-line-contents virtual" style="transform: translateY(260px); min-height: auto;"><div><div id="LC14" class="react-file-line html-div" data-testid="code-cell" data-line-number="14" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x80"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text="],"></span></div></div></div><div data-key="14" class="child-of-line-6  react-code-text react-code-line-contents virtual" style="transform: translateY(280px); min-height: auto;"><div><div id="LC15" class="react-file-line html-div" data-testid="code-cell" data-line-number="15" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x1b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text="],"></span></div></div></div><div data-key="15" class="child-of-line-6  react-code-text react-code-line-contents virtual" style="transform: translateY(300px); min-height: auto;"><div><div id="LC16" class="react-file-line html-div" data-testid="code-cell" data-line-number="16" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x36"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text="],"></span></div></div></div><div data-key="16" class="react-code-text react-code-line-contents virtual" style="transform: translateY(320px); min-height: auto;"><div><div id="LC17" class="react-file-line html-div" data-testid="code-cell" data-line-number="17" style="position: relative;"><span data-code-text="])"></span></div></div></div><div data-key="17" class="react-code-text react-code-line-contents virtual" style="transform: translateY(340px); min-height: auto;"><div><div id="LC18" class="react-file-line html-div" data-testid="code-cell" data-line-number="18" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="18" class="react-code-text react-code-line-contents virtual" style="transform: translateY(360px); min-height: auto;"><div><div id="LC19" class="react-file-line html-div" data-testid="code-cell" data-line-number="19" style="position: relative;"><span class="pl-s1" data-code-text="roundConstant_8"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="np"></span><span data-code-text="."></span><span class="pl-en" data-code-text="array"></span><span data-code-text="(["></span></div></div></div><div data-key="19" class="child-of-line-19  react-code-text react-code-line-contents virtual" style="transform: translateY(380px); min-height: auto;"><div><div id="LC20" class="react-file-line html-div" data-testid="code-cell" data-line-number="20" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text="],"></span></div></div></div><div data-key="20" class="child-of-line-19  react-code-text react-code-line-contents virtual" style="transform: translateY(400px); min-height: auto;"><div><div id="LC21" class="react-file-line html-div" data-testid="code-cell" data-line-number="21" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x02"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text="],"></span></div></div></div><div data-key="21" class="child-of-line-19  react-code-text react-code-line-contents virtual" style="transform: translateY(420px); min-height: auto;"><div><div id="LC22" class="react-file-line html-div" data-testid="code-cell" data-line-number="22" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x04"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text="],"></span></div></div></div><div data-key="22" class="child-of-line-19  react-code-text react-code-line-contents virtual" style="transform: translateY(440px); min-height: auto;"><div><div id="LC23" class="react-file-line html-div" data-testid="code-cell" data-line-number="23" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x08"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text="],"></span></div></div></div><div data-key="23" class="child-of-line-19  react-code-text react-code-line-contents virtual" style="transform: translateY(460px); min-height: auto;"><div><div id="LC24" class="react-file-line html-div" data-testid="code-cell" data-line-number="24" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x10"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text="],"></span></div></div></div><div data-key="24" class="child-of-line-19  react-code-text react-code-line-contents virtual" style="transform: translateY(480px); min-height: auto;"><div><div id="LC25" class="react-file-line html-div" data-testid="code-cell" data-line-number="25" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x20"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text="],"></span></div></div></div><div data-key="25" class="child-of-line-19  react-code-text react-code-line-contents virtual" style="transform: translateY(500px); min-height: auto;"><div><div id="LC26" class="react-file-line html-div" data-testid="code-cell" data-line-number="26" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x40"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text="],"></span></div></div></div><div data-key="26" class="child-of-line-19  react-code-text react-code-line-contents virtual" style="transform: translateY(520px); min-height: auto;"><div><div id="LC27" class="react-file-line html-div" data-testid="code-cell" data-line-number="27" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x80"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text="],"></span></div></div></div><div data-key="27" class="child-of-line-19  react-code-text react-code-line-contents virtual" style="transform: translateY(540px); min-height: auto;"><div><div id="LC28" class="react-file-line html-div" data-testid="code-cell" data-line-number="28" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x1b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text="],"></span></div></div></div><div data-key="28" class="child-of-line-19  react-code-text react-code-line-contents virtual" style="transform: translateY(560px); min-height: auto;"><div><div id="LC29" class="react-file-line html-div" data-testid="code-cell" data-line-number="29" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x36"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text="],"></span></div></div></div><div data-key="29" class="react-code-text react-code-line-contents virtual" style="transform: translateY(580px); min-height: auto;"><div><div id="LC30" class="react-file-line html-div" data-testid="code-cell" data-line-number="30" style="position: relative;"><span data-code-text="])"></span></div></div></div><div data-key="30" class="react-code-text react-code-line-contents virtual" style="transform: translateY(600px); min-height: auto;"><div><div id="LC31" class="react-file-line html-div" data-testid="code-cell" data-line-number="31" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="31" class="react-code-text react-code-line-contents virtual" style="transform: translateY(620px); min-height: auto;"><div><div id="LC32" class="react-file-line html-div" data-testid="code-cell" data-line-number="32" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="32" class="react-code-text react-code-line-contents virtual" style="transform: translateY(640px); min-height: auto;"><div><div id="LC33" class="react-file-line html-div" data-testid="code-cell" data-line-number="33" style="position: relative;"><span class="pl-c" data-code-text="# Substitution Box: Encryption"></span></div></div></div><div data-key="33" class="react-code-text react-code-line-contents virtual" style="transform: translateY(660px); min-height: auto;"><div><div id="LC34" class="react-file-line html-div" data-testid="code-cell" data-line-number="34" style="position: relative;"><span class="pl-s1" data-code-text="s_box"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="np"></span><span data-code-text="."></span><span class="pl-en" data-code-text="array"></span><span data-code-text="(["></span></div></div></div><div data-key="34" class="child-of-line-34  react-code-text react-code-line-contents virtual" style="transform: translateY(680px); min-height: auto;"><div><div id="LC35" class="react-file-line html-div" data-testid="code-cell" data-line-number="35" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x63"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x7c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x77"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x7b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xf2"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x6b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x6f"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xc5"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x30"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x67"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x2b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xfe"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xd7"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xab"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x76"></span><span data-code-text="],"></span></div></div></div><div data-key="35" class="child-of-line-34  react-code-text react-code-line-contents virtual" style="transform: translateY(700px); min-height: auto;"><div><div id="LC36" class="react-file-line html-div" data-testid="code-cell" data-line-number="36" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0xca"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x82"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xc9"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x7d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xfa"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x59"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x47"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xf0"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xad"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xd4"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xa2"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xaf"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x9c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xa4"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x72"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xc0"></span><span data-code-text="],"></span></div></div></div><div data-key="36" class="child-of-line-34  react-code-text react-code-line-contents virtual" style="transform: translateY(720px); min-height: auto;"><div><div id="LC37" class="react-file-line html-div" data-testid="code-cell" data-line-number="37" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0xb7"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xfd"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x93"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x26"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x36"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x3f"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xf7"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xcc"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x34"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xa5"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xe5"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xf1"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x71"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xd8"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x31"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x15"></span><span data-code-text="],"></span></div></div></div><div data-key="37" class="child-of-line-34  react-code-text react-code-line-contents virtual" style="transform: translateY(740px); min-height: auto;"><div><div id="LC38" class="react-file-line html-div" data-testid="code-cell" data-line-number="38" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x04"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xc7"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x23"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xc3"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x18"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x96"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x05"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x9a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x07"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x12"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x80"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xe2"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xeb"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x27"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xb2"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x75"></span><span data-code-text="],"></span></div></div></div><div data-key="38" class="child-of-line-34  react-code-text react-code-line-contents virtual" style="transform: translateY(760px); min-height: auto;"><div><div id="LC39" class="react-file-line html-div" data-testid="code-cell" data-line-number="39" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x09"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x83"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x2c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x1a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x1b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x6e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x5a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xa0"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x52"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x3b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xd6"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xb3"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x29"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xe3"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x2f"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x84"></span><span data-code-text="],"></span></div></div></div><div data-key="39" class="child-of-line-34  react-code-text react-code-line-contents virtual" style="transform: translateY(780px); min-height: auto;"><div><div id="LC40" class="react-file-line html-div" data-testid="code-cell" data-line-number="40" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x53"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xd1"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xed"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x20"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xfc"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xb1"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x5b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x6a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xcb"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xbe"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x39"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x4a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x4c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x58"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xcf"></span><span data-code-text="],"></span></div></div></div><div data-key="40" class="child-of-line-34  react-code-text react-code-line-contents virtual" style="transform: translateY(800px); min-height: auto;"><div><div id="LC41" class="react-file-line html-div" data-testid="code-cell" data-line-number="41" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0xd0"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xef"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xaa"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xfb"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x43"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x4d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x33"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x85"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x45"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xf9"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x02"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x7f"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x50"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x3c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x9f"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xa8"></span><span data-code-text="],"></span></div></div></div><div data-key="41" class="child-of-line-34  react-code-text react-code-line-contents virtual" style="transform: translateY(820px); min-height: auto;"><div><div id="LC42" class="react-file-line html-div" data-testid="code-cell" data-line-number="42" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x51"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xa3"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x40"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x8f"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x92"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x9d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x38"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xf5"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xbc"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xb6"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xda"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x21"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x10"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xff"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xf3"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xd2"></span><span data-code-text="],"></span></div></div></div><div data-key="42" class="child-of-line-34  react-code-text react-code-line-contents virtual" style="transform: translateY(840px); min-height: auto;"><div><div id="LC43" class="react-file-line html-div" data-testid="code-cell" data-line-number="43" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0xcd"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x13"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xec"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x5f"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x97"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x44"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x17"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xc4"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xa7"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x7e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x3d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x64"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x5d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x19"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x73"></span><span data-code-text="],"></span></div></div></div><div data-key="43" class="child-of-line-34  react-code-text react-code-line-contents virtual" style="transform: translateY(860px); min-height: auto;"><div><div id="LC44" class="react-file-line html-div" data-testid="code-cell" data-line-number="44" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x60"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x81"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x4f"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xdc"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x22"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x2a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x90"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x88"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x46"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xee"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xb8"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x14"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xde"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x5e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xdb"></span><span data-code-text="],"></span></div></div></div><div data-key="44" class="child-of-line-34  react-code-text react-code-line-contents virtual" style="transform: translateY(880px); min-height: auto;"><div><div id="LC45" class="react-file-line html-div" data-testid="code-cell" data-line-number="45" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0xe0"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x32"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x3a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x49"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x06"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x24"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x5c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xc2"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xd3"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xac"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x62"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x91"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x95"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xe4"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x79"></span><span data-code-text="],"></span></div></div></div><div data-key="45" class="child-of-line-34  react-code-text react-code-line-contents virtual" style="transform: translateY(900px); min-height: auto;"><div><div id="LC46" class="react-file-line html-div" data-testid="code-cell" data-line-number="46" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0xe7"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xc8"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x37"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x6d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x8d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xd5"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x4e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xa9"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x6c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x56"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xf4"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xea"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x65"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x7a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xae"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x08"></span><span data-code-text="],"></span></div></div></div><div data-key="46" class="child-of-line-34  react-code-text react-code-line-contents virtual" style="transform: translateY(920px); min-height: auto;"><div><div id="LC47" class="react-file-line html-div" data-testid="code-cell" data-line-number="47" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0xba"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x78"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x25"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x2e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x1c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xa6"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xb4"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xc6"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xe8"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xdd"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x74"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x1f"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x4b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xbd"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x8b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x8a"></span><span data-code-text="],"></span></div></div></div><div data-key="47" class="child-of-line-34  react-code-text react-code-line-contents virtual" style="transform: translateY(940px); min-height: auto;"><div><div id="LC48" class="react-file-line html-div" data-testid="code-cell" data-line-number="48" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x70"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x3e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xb5"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x66"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x48"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x03"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xf6"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x61"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x35"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x57"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xb9"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x86"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xc1"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x1d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x9e"></span><span data-code-text="],"></span></div></div></div><div data-key="48" class="child-of-line-34  react-code-text react-code-line-contents virtual" style="transform: translateY(960px); min-height: auto;"><div><div id="LC49" class="react-file-line html-div" data-testid="code-cell" data-line-number="49" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0xe1"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xf8"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x98"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x11"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x69"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xd9"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x8e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x94"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x9b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x1e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x87"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xe9"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xce"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x55"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x28"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xdf"></span><span data-code-text="],"></span></div></div></div><div data-key="49" class="child-of-line-34  react-code-text react-code-line-contents virtual" style="transform: translateY(980px); min-height: auto;"><div><div id="LC50" class="react-file-line html-div" data-testid="code-cell" data-line-number="50" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x8c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xa1"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x89"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xbf"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xe6"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x42"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x68"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x41"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x99"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x2d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0f"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xb0"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x54"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xbb"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x16"></span><span data-code-text="],"></span></div></div></div><div data-key="50" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1000px); min-height: auto;"><div><div id="LC51" class="react-file-line html-div" data-testid="code-cell" data-line-number="51" style="position: relative;"><span data-code-text="])"></span></div></div></div><div data-key="51" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1020px); min-height: auto;"><div><div id="LC52" class="react-file-line html-div" data-testid="code-cell" data-line-number="52" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="52" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1040px); min-height: auto;"><div><div id="LC53" class="react-file-line html-div" data-testid="code-cell" data-line-number="53" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="53" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1060px); min-height: auto;"><div><div id="LC54" class="react-file-line html-div" data-testid="code-cell" data-line-number="54" style="position: relative;"><span class="pl-c" data-code-text="# Substitution Box: Decryption"></span></div></div></div><div data-key="54" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1080px); min-height: auto;"><div><div id="LC55" class="react-file-line html-div" data-testid="code-cell" data-line-number="55" style="position: relative;"><span class="pl-s1" data-code-text="invs_box"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="np"></span><span data-code-text="."></span><span class="pl-en" data-code-text="array"></span><span data-code-text="(["></span></div></div></div><div data-key="55" class="child-of-line-55  react-code-text react-code-line-contents virtual" style="transform: translateY(1100px); min-height: auto;"><div><div id="LC56" class="react-file-line html-div" data-testid="code-cell" data-line-number="56" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x52"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x09"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x6a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xd5"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x30"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x36"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xa5"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x38"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xbf"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x40"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xa3"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x9e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x81"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xf3"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xd7"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xfb"></span><span data-code-text="],"></span></div></div></div><div data-key="56" class="child-of-line-55  react-code-text react-code-line-contents virtual" style="transform: translateY(1120px); min-height: auto;"><div><div id="LC57" class="react-file-line html-div" data-testid="code-cell" data-line-number="57" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x7c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xe3"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x39"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x82"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x9b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x2f"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xff"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x87"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x34"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x8e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x43"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x44"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xc4"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xde"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xe9"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xcb"></span><span data-code-text="],"></span></div></div></div><div data-key="57" class="child-of-line-55  react-code-text react-code-line-contents virtual" style="transform: translateY(1140px); min-height: auto;"><div><div id="LC58" class="react-file-line html-div" data-testid="code-cell" data-line-number="58" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x54"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x7b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x94"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x32"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xa6"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xc2"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x23"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x3d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xee"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x4c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x95"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x42"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xfa"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xc3"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x4e"></span><span data-code-text="],"></span></div></div></div><div data-key="58" class="child-of-line-55  react-code-text react-code-line-contents virtual" style="transform: translateY(1160px); min-height: auto;"><div><div id="LC59" class="react-file-line html-div" data-testid="code-cell" data-line-number="59" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x08"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x2e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xa1"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x66"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x28"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xd9"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x24"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xb2"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x76"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x5b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xa2"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x49"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x6d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x8b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xd1"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x25"></span><span data-code-text="],"></span></div></div></div><div data-key="59" class="child-of-line-55  react-code-text react-code-line-contents virtual" style="transform: translateY(1180px); min-height: auto;"><div><div id="LC60" class="react-file-line html-div" data-testid="code-cell" data-line-number="60" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x72"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xf8"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xf6"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x64"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x86"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x68"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x98"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x16"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xd4"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xa4"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x5c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xcc"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x5d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x65"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xb6"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x92"></span><span data-code-text="],"></span></div></div></div><div data-key="60" class="child-of-line-55  react-code-text react-code-line-contents virtual" style="transform: translateY(1200px); min-height: auto;"><div><div id="LC61" class="react-file-line html-div" data-testid="code-cell" data-line-number="61" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x6c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x70"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x48"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x50"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xfd"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xed"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xb9"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xda"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x5e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x15"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x46"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x57"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xa7"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x8d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x9d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x84"></span><span data-code-text="],"></span></div></div></div><div data-key="61" class="child-of-line-55  react-code-text react-code-line-contents virtual" style="transform: translateY(1220px); min-height: auto;"><div><div id="LC62" class="react-file-line html-div" data-testid="code-cell" data-line-number="62" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x90"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xd8"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xab"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x8c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xbc"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xd3"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xf7"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xe4"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x58"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x05"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xb8"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xb3"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x45"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x06"></span><span data-code-text="],"></span></div></div></div><div data-key="62" class="child-of-line-55  react-code-text react-code-line-contents virtual" style="transform: translateY(1240px); min-height: auto;"><div><div id="LC63" class="react-file-line html-div" data-testid="code-cell" data-line-number="63" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0xd0"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x2c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x1e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x8f"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xca"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x3f"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0f"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x02"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xc1"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xaf"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xbd"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x03"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x13"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x8a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x6b"></span><span data-code-text="],"></span></div></div></div><div data-key="63" class="child-of-line-55  react-code-text react-code-line-contents virtual" style="transform: translateY(1260px); min-height: auto;"><div><div id="LC64" class="react-file-line html-div" data-testid="code-cell" data-line-number="64" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x3a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x91"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x11"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x41"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x4f"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x67"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xdc"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xea"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x97"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xf2"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xcf"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xce"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xf0"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xb4"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xe6"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x73"></span><span data-code-text="],"></span></div></div></div><div data-key="64" class="child-of-line-55  react-code-text react-code-line-contents virtual" style="transform: translateY(1280px); min-height: auto;"><div><div id="LC65" class="react-file-line html-div" data-testid="code-cell" data-line-number="65" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x96"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xac"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x74"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x22"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xe7"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xad"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x35"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x85"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xe2"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xf9"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x37"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xe8"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x1c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x75"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xdf"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x6e"></span><span data-code-text="],"></span></div></div></div><div data-key="65" class="child-of-line-55  react-code-text react-code-line-contents virtual" style="transform: translateY(1300px); min-height: auto;"><div><div id="LC66" class="react-file-line html-div" data-testid="code-cell" data-line-number="66" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x47"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xf1"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x1a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x71"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x1d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x29"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xc5"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x89"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x6f"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xb7"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x62"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xaa"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x18"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xbe"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x1b"></span><span data-code-text="],"></span></div></div></div><div data-key="66" class="child-of-line-55  react-code-text react-code-line-contents virtual" style="transform: translateY(1320px); min-height: auto;"><div><div id="LC67" class="react-file-line html-div" data-testid="code-cell" data-line-number="67" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0xfc"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x56"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x3e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x4b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xc6"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xd2"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x79"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x20"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x9a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xdb"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xc0"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xfe"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x78"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xcd"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x5a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xf4"></span><span data-code-text="],"></span></div></div></div><div data-key="67" class="child-of-line-55  react-code-text react-code-line-contents virtual" style="transform: translateY(1340px); min-height: auto;"><div><div id="LC68" class="react-file-line html-div" data-testid="code-cell" data-line-number="68" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x1f"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xdd"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xa8"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x33"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x88"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x07"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xc7"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x31"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xb1"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x12"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x10"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x59"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x27"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x80"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xec"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x5f"></span><span data-code-text="],"></span></div></div></div><div data-key="68" class="child-of-line-55  react-code-text react-code-line-contents virtual" style="transform: translateY(1360px); min-height: auto;"><div><div id="LC69" class="react-file-line html-div" data-testid="code-cell" data-line-number="69" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x60"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x51"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x7f"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xa9"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x19"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xb5"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x4a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x2d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xe5"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x7a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x9f"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x93"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xc9"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x9c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xef"></span><span data-code-text="],"></span></div></div></div><div data-key="69" class="child-of-line-55  react-code-text react-code-line-contents virtual" style="transform: translateY(1380px); min-height: auto;"><div><div id="LC70" class="react-file-line html-div" data-testid="code-cell" data-line-number="70" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0xa0"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xe0"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x3b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x4d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xae"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x2a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xf5"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xb0"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xc8"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xeb"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xbb"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x3c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x83"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x53"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x99"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x61"></span><span data-code-text="],"></span></div></div></div><div data-key="70" class="child-of-line-55  react-code-text react-code-line-contents virtual" style="transform: translateY(1400px); min-height: auto;"><div><div id="LC71" class="react-file-line html-div" data-testid="code-cell" data-line-number="71" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x17"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x2b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x04"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x7e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xba"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x77"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xd6"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x26"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0xe1"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x69"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x14"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x63"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x55"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x21"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x7d"></span><span data-code-text="],"></span></div></div></div><div data-key="71" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1420px); min-height: auto;"><div><div id="LC72" class="react-file-line html-div" data-testid="code-cell" data-line-number="72" style="position: relative;"><span data-code-text="])"></span></div></div></div><div data-key="72" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1440px); min-height: auto;"><div><div id="LC73" class="react-file-line html-div" data-testid="code-cell" data-line-number="73" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="73" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1460px); min-height: auto;"><div><div id="LC74" class="react-file-line html-div" data-testid="code-cell" data-line-number="74" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="74" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1480px); min-height: auto;"><div><div id="LC75" class="react-file-line html-div" data-testid="code-cell" data-line-number="75" style="position: relative;"><span class="pl-c" data-code-text="# Rijndael Galois Field: Encryption"></span></div></div></div><div data-key="75" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1500px); min-height: auto;"><div><div id="LC76" class="react-file-line html-div" data-testid="code-cell" data-line-number="76" style="position: relative;"><span class="pl-s1" data-code-text="encryptMDS"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="np"></span><span data-code-text="."></span><span class="pl-en" data-code-text="array"></span><span data-code-text="(["></span></div></div></div><div data-key="76" class="child-of-line-76  react-code-text react-code-line-contents virtual" style="transform: translateY(1520px); min-height: auto;"><div><div id="LC77" class="react-file-line html-div" data-testid="code-cell" data-line-number="77" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x02"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x03"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text="],"></span></div></div></div><div data-key="77" class="child-of-line-76  react-code-text react-code-line-contents virtual" style="transform: translateY(1540px); min-height: auto;"><div><div id="LC78" class="react-file-line html-div" data-testid="code-cell" data-line-number="78" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x02"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x03"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text="],"></span></div></div></div><div data-key="78" class="child-of-line-76  react-code-text react-code-line-contents virtual" style="transform: translateY(1560px); min-height: auto;"><div><div id="LC79" class="react-file-line html-div" data-testid="code-cell" data-line-number="79" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x02"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x03"></span><span data-code-text="],"></span></div></div></div><div data-key="79" class="child-of-line-76  react-code-text react-code-line-contents virtual" style="transform: translateY(1580px); min-height: auto;"><div><div id="LC80" class="react-file-line html-div" data-testid="code-cell" data-line-number="80" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x03"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x02"></span><span data-code-text="],"></span></div></div></div><div data-key="80" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1600px); min-height: auto;"><div><div id="LC81" class="react-file-line html-div" data-testid="code-cell" data-line-number="81" style="position: relative;"><span data-code-text="])"></span></div></div></div><div data-key="81" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1620px); min-height: auto;"><div><div id="LC82" class="react-file-line html-div" data-testid="code-cell" data-line-number="82" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="82" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1640px); min-height: auto;"><div><div id="LC83" class="react-file-line html-div" data-testid="code-cell" data-line-number="83" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="83" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1660px); min-height: auto;"><div><div id="LC84" class="react-file-line html-div" data-testid="code-cell" data-line-number="84" style="position: relative;"><span class="pl-c" data-code-text="# Rijndael Galois Field: Encryption 8*8"></span></div></div></div><div data-key="84" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1680px); min-height: auto;"><div><div id="LC85" class="react-file-line html-div" data-testid="code-cell" data-line-number="85" style="position: relative;"><span class="pl-s1" data-code-text="encryptMDS_8"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="np"></span><span data-code-text="."></span><span class="pl-en" data-code-text="array"></span><span data-code-text="(["></span></div></div></div><div data-key="85" class="child-of-line-85  react-code-text react-code-line-contents virtual" style="transform: translateY(1700px); min-height: auto;"><div><div id="LC86" class="react-file-line html-div" data-testid="code-cell" data-line-number="86" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x02"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x03"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text="],"></span></div></div></div><div data-key="86" class="child-of-line-85  react-code-text react-code-line-contents virtual" style="transform: translateY(1720px); min-height: auto;"><div><div id="LC87" class="react-file-line html-div" data-testid="code-cell" data-line-number="87" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x03"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x02"></span><span data-code-text="],"></span></div></div></div><div data-key="87" class="child-of-line-85  react-code-text react-code-line-contents virtual" style="transform: translateY(1740px); min-height: auto;"><div><div id="LC88" class="react-file-line html-div" data-testid="code-cell" data-line-number="88" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x03"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x02"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text="],"></span></div></div></div><div data-key="88" class="child-of-line-85  react-code-text react-code-line-contents virtual" style="transform: translateY(1760px); min-height: auto;"><div><div id="LC89" class="react-file-line html-div" data-testid="code-cell" data-line-number="89" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x02"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x03"></span><span data-code-text="],"></span></div></div></div><div data-key="89" class="child-of-line-85  react-code-text react-code-line-contents virtual" style="transform: translateY(1780px); min-height: auto;"><div><div id="LC90" class="react-file-line html-div" data-testid="code-cell" data-line-number="90" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x02"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x03"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text="],"></span></div></div></div><div data-key="90" class="child-of-line-85  react-code-text react-code-line-contents virtual" style="transform: translateY(1800px); min-height: auto;"><div><div id="LC91" class="react-file-line html-div" data-testid="code-cell" data-line-number="91" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x02"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x03"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text="],"></span></div></div></div><div data-key="91" class="child-of-line-85  react-code-text react-code-line-contents virtual" style="transform: translateY(1820px); min-height: auto;"><div><div id="LC92" class="react-file-line html-div" data-testid="code-cell" data-line-number="92" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x02"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x03"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text="],"></span></div></div></div><div data-key="92" class="child-of-line-85  react-code-text react-code-line-contents virtual" style="transform: translateY(1840px); min-height: auto;"><div><div id="LC93" class="react-file-line html-div" data-testid="code-cell" data-line-number="93" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x02"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x03"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text="],"></span></div></div></div><div data-key="93" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1860px); min-height: auto;"><div><div id="LC94" class="react-file-line html-div" data-testid="code-cell" data-line-number="94" style="position: relative;"><span data-code-text="])"></span></div></div></div><div data-key="94" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1880px); min-height: auto;"><div><div id="LC95" class="react-file-line html-div" data-testid="code-cell" data-line-number="95" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="95" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1900px); min-height: auto;"><div><div id="LC96" class="react-file-line html-div" data-testid="code-cell" data-line-number="96" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="96" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1920px); min-height: auto;"><div><div id="LC97" class="react-file-line html-div" data-testid="code-cell" data-line-number="97" style="position: relative;"><span class="pl-c" data-code-text="# Rijndael Galois Field: Decryption"></span></div></div></div><div data-key="97" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1940px); min-height: auto;"><div><div id="LC98" class="react-file-line html-div" data-testid="code-cell" data-line-number="98" style="position: relative;"><span class="pl-s1" data-code-text="decryptMDS"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="np"></span><span data-code-text="."></span><span class="pl-en" data-code-text="array"></span><span data-code-text="(["></span></div></div></div><div data-key="98" class="child-of-line-98  react-code-text react-code-line-contents virtual" style="transform: translateY(1960px); min-height: auto;"><div><div id="LC99" class="react-file-line html-div" data-testid="code-cell" data-line-number="99" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x0e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x09"></span><span data-code-text="],"></span></div></div></div><div data-key="99" class="child-of-line-98  react-code-text react-code-line-contents virtual" style="transform: translateY(1980px); min-height: auto;"><div><div id="LC100" class="react-file-line html-div" data-testid="code-cell" data-line-number="100" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x09"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0d"></span><span data-code-text="],"></span></div></div></div><div data-key="100" class="child-of-line-98  react-code-text react-code-line-contents virtual" style="transform: translateY(2000px); min-height: auto;"><div><div id="LC101" class="react-file-line html-div" data-testid="code-cell" data-line-number="101" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x0d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x09"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0b"></span><span data-code-text="],"></span></div></div></div><div data-key="101" class="child-of-line-98  react-code-text react-code-line-contents virtual" style="transform: translateY(2020px); min-height: auto;"><div><div id="LC102" class="react-file-line html-div" data-testid="code-cell" data-line-number="102" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x0b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x09"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0e"></span><span data-code-text="],"></span></div></div></div><div data-key="102" class="react-code-text react-code-line-contents virtual" style="transform: translateY(2040px); min-height: auto;"><div><div id="LC103" class="react-file-line html-div" data-testid="code-cell" data-line-number="103" style="position: relative;"><span data-code-text="])"></span></div></div></div><div data-key="103" class="react-code-text react-code-line-contents virtual" style="transform: translateY(2060px); min-height: auto;"><div><div id="LC104" class="react-file-line html-div" data-testid="code-cell" data-line-number="104" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="104" class="react-code-text react-code-line-contents virtual" style="transform: translateY(2080px); min-height: auto;"><div><div id="LC105" class="react-file-line html-div" data-testid="code-cell" data-line-number="105" style="position: relative;"><span class="pl-c" data-code-text="# Rijndael Galois Field: Decryption 8*8"></span></div></div></div><div data-key="105" class="react-code-text react-code-line-contents virtual" style="transform: translateY(2100px); min-height: auto;"><div><div id="LC106" class="react-file-line html-div" data-testid="code-cell" data-line-number="106" style="position: relative;"><span class="pl-s1" data-code-text="decryptMDS_8"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="np"></span><span data-code-text="."></span><span class="pl-en" data-code-text="array"></span><span data-code-text="(["></span></div></div></div><div data-key="106" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2120px); min-height: auto;"><div><div id="LC107" class="react-file-line html-div" data-testid="code-cell" data-line-number="107" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x0e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x09"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text="],"></span></div></div></div><div data-key="107" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2140px); min-height: auto;"><div><div id="LC108" class="react-file-line html-div" data-testid="code-cell" data-line-number="108" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x09"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0e"></span><span data-code-text="],"></span></div></div></div><div data-key="108" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2160px); min-height: auto;"><div><div id="LC109" class="react-file-line html-div" data-testid="code-cell" data-line-number="109" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x09"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text="],"></span></div></div></div><div data-key="109" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2180px); min-height: auto;"><div><div id="LC110" class="react-file-line html-div" data-testid="code-cell" data-line-number="110" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x09"></span><span data-code-text="],"></span></div></div></div><div data-key="110" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2200px); min-height: auto;"><div><div id="LC111" class="react-file-line html-div" data-testid="code-cell" data-line-number="111" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x0d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x09"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text="],"></span></div></div></div><div data-key="111" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2220px); min-height: auto;"><div><div id="LC112" class="react-file-line html-div" data-testid="code-cell" data-line-number="112" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x09"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0d"></span><span data-code-text="],"></span></div></div></div><div data-key="112" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2240px); min-height: auto;"><div><div id="LC113" class="react-file-line html-div" data-testid="code-cell" data-line-number="113" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x0b"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x09"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text="],"></span></div></div></div><div data-key="113" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2260px); min-height: auto;"><div><div id="LC114" class="react-file-line html-div" data-testid="code-cell" data-line-number="114" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x09"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0d"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x01"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0b"></span><span data-code-text="],"></span></div></div></div><div data-key="114" class="react-code-text react-code-line-contents virtual" style="transform: translateY(2280px); min-height: auto;"><div><div id="LC115" class="react-file-line html-div" data-testid="code-cell" data-line-number="115" style="position: relative;"><span data-code-text="])"></span></div></div></div><div data-key="115" class="react-code-text react-code-line-contents virtual" style="transform: translateY(2300px); min-height: auto;"><div><div id="LC116" class="react-file-line html-div" data-testid="code-cell" data-line-number="116" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="116" class="react-code-text react-code-line-contents virtual" style="transform: translateY(2320px); min-height: auto;"><div><div id="LC117" class="react-file-line html-div" data-testid="code-cell" data-line-number="117" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="117" class="react-code-text react-code-line-contents virtual" style="transform: translateY(2340px); min-height: auto;"><div><div id="LC118" class="react-file-line html-div" data-testid="code-cell" data-line-number="118" style="position: relative;"><span class="pl-c" data-code-text="# Look UP Table Mix Column:"></span></div></div></div><div data-key="118" class="react-code-text react-code-line-contents virtual" style="transform: translateY(2360px); min-height: auto;"><div><div id="LC119" class="react-file-line html-div" data-testid="code-cell" data-line-number="119" style="position: relative;"><span class="pl-s1" data-code-text="mc2"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="np"></span><span data-code-text="."></span><span class="pl-en" data-code-text="array"></span><span data-code-text="(["></span></div></div></div><div data-key="119" class="child-of-line-119  react-code-text react-code-line-contents virtual" style="transform: translateY(2380px); min-height: auto;"><div><div id="LC120" class="react-file-line html-div" data-testid="code-cell" data-line-number="120" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x00"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x02"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x04"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x06"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x08"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x0e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x10"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x12"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x14"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x16"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x18"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x1a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x1c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x1e"></span><span data-code-text="],"></span></div></div></div><div data-key="120" class="child-of-line-119  react-code-text react-code-line-contents virtual" style="transform: translateY(2400px); min-height: auto;"><div><div id="LC121" class="react-file-line html-div" data-testid="code-cell" data-line-number="121" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x20"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x22"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x24"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x26"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x28"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x2a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x2c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x2e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x30"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x32"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x34"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x36"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x38"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x3a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x3c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x3e"></span><span data-code-text="],"></span></div></div></div><div data-key="121" class="child-of-line-119  react-code-text react-code-line-contents virtual" style="transform: translateY(2420px); min-height: auto;"><div><div id="LC122" class="react-file-line html-div" data-testid="code-cell" data-line-number="122" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x40"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x42"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x44"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x46"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x48"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x4a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x4c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x4e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x50"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x52"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x54"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x56"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x58"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x5a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x5c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x5e"></span><span data-code-text="],"></span></div></div></div><div data-key="122" class="child-of-line-119  react-code-text react-code-line-contents virtual" style="transform: translateY(2440px); min-height: auto;"><div><div id="LC123" class="react-file-line html-div" data-testid="code-cell" data-line-number="123" style="position: relative;"><span data-code-text="    ["></span><span class="pl-c1" data-code-text="0x60"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x62"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x64"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x66"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x68"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x6a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x6c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x6e"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x70"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x72"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x74"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x76"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x78"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x7a"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x7c"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="0x7e"></span><span data-code-text="],"></span></div></div></div><div data-key="510" class="child-of-line-390 child-of-line-496  react-code-text react-code-line-contents virtual" style="transform: translateY(10200px); min-height: auto;"><div><div id="LC511" class="react-file-line html-div" data-testid="code-cell" data-line-number="511" style="position: relative;"><span data-code-text="            "></span><span class="pl-k" data-code-text="return"></span><span data-code-text=" "></span><span class="pl-s"><span data-code-text="f&#39;"></span><span class="pl-s1"><span class="pl-kos" data-code-text="{"></span><span class="pl-en" data-code-text="int"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="hex_ecrypt"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="16"></span><span data-code-text="):0&gt;b"></span><span class="pl-kos" data-code-text="}"></span></span><span data-code-text="&#39;"></span></span></div></div></div><div data-key="511" class="child-of-line-390 child-of-line-496  react-code-text react-code-line-contents virtual" style="transform: translateY(10220px); min-height: auto;"><div><div id="LC512" class="react-file-line html-div" data-testid="code-cell" data-line-number="512" style="position: relative;"><span data-code-text="        "></span><span class="pl-k" data-code-text="if"></span><span data-code-text=" ("></span><span class="pl-s1" data-code-text="type"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="=="></span><span data-code-text=" "></span><span class="pl-s" data-code-text="&#39;__all__&#39;"></span><span data-code-text="):"></span></div></div></div><div data-key="512" class="child-of-line-390 child-of-line-496  react-code-text react-code-line-contents virtual" style="transform: translateY(10240px); min-height: auto;"><div><div id="LC513" class="react-file-line html-div" data-testid="code-cell" data-line-number="513" style="position: relative;"><span data-code-text="            "></span><span class="pl-k" data-code-text="return"></span><span data-code-text=" {"></span></div></div></div><div data-key="513" class="child-of-line-390 child-of-line-496  react-code-text react-code-line-contents virtual" style="transform: translateY(10260px); min-height: auto;"><div><div id="LC514" class="react-file-line html-div" data-testid="code-cell" data-line-number="514" style="position: relative;"><span data-code-text="                "></span><span class="pl-s" data-code-text="&#39;hex&#39;"></span><span data-code-text=": "></span><span class="pl-s1" data-code-text="hex_ecrypt"></span><span data-code-text=","></span></div></div></div><div data-key="514" class="child-of-line-390 child-of-line-496  react-code-text react-code-line-contents virtual" style="transform: translateY(10280px); min-height: auto;"><div><div id="LC515" class="react-file-line html-div" data-testid="code-cell" data-line-number="515" style="position: relative;"><span data-code-text="                "></span><span class="pl-s" data-code-text="&#39;b64&#39;"></span><span data-code-text=": "></span><span class="pl-en" data-code-text="b64encode"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="bytes"></span><span data-code-text="."></span><span class="pl-en" data-code-text="fromhex"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="hex_ecrypt"></span><span data-code-text="))."></span><span class="pl-en" data-code-text="decode"></span><span data-code-text="(),"></span></div></div></div><div data-key="515" class="child-of-line-390 child-of-line-496  react-code-text react-code-line-contents virtual" style="transform: translateY(10300px); min-height: auto;"><div><div id="LC516" class="react-file-line html-div" data-testid="code-cell" data-line-number="516" style="position: relative;"><span data-code-text="                "></span><span class="pl-s" data-code-text="&#39;0b&#39;"></span><span data-code-text=": "></span><span class="pl-en" data-code-text="bin"></span><span data-code-text="("></span><span class="pl-en" data-code-text="int"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="hex_ecrypt"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="16"></span><span data-code-text="))["></span><span class="pl-c1" data-code-text="2"></span><span data-code-text=":]."></span><span class="pl-en" data-code-text="zfill"></span><span data-code-text="("></span><span class="pl-en" data-code-text="len"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="hex_ecrypt"></span><span data-code-text=") "></span><span class="pl-c1" data-code-text="*"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="4"></span><span data-code-text=")"></span></div></div></div><div data-key="516" class="child-of-line-390 child-of-line-496  react-code-text react-code-line-contents virtual" style="transform: translateY(10320px); min-height: auto;"><div><div id="LC517" class="react-file-line html-div" data-testid="code-cell" data-line-number="517" style="position: relative;"><span data-code-text="            }"></span></div></div></div><div data-key="517" class="child-of-line-390  react-code-text react-code-line-contents virtual" style="transform: translateY(10340px); min-height: auto;"><div><div id="LC518" class="react-file-line html-div" data-testid="code-cell" data-line-number="518" style="position: relative;"><span data-code-text="        "></span><span class="pl-k" data-code-text="return"></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="hex_ecrypt"></span></div></div></div><div data-key="518" class="child-of-line-390  react-code-text react-code-line-contents virtual" style="transform: translateY(10360px); min-height: auto;"><div><div id="LC519" class="react-file-line html-div" data-testid="code-cell" data-line-number="519" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="519" class="child-of-line-390  react-code-text react-code-line-contents virtual" style="transform: translateY(10380px); min-height: auto;"><div><div id="LC520" class="react-file-line html-div" data-testid="code-cell" data-line-number="520" style="position: relative;"><span data-code-text="    "></span><span class="pl-c" data-code-text="# Decryption"></span></div></div></div><div data-key="520" class="child-of-line-390  react-code-text react-code-line-contents virtual" style="transform: translateY(10400px); min-height: auto;"><div><div id="LC521" class="react-file-line html-div" data-testid="code-cell" data-line-number="521" style="position: relative;"><span data-code-text="    "></span><span class="pl-k" data-code-text="def"></span><span data-code-text=" "></span><span class="pl-en" data-code-text="decrypt"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="self"></span><span data-code-text=", "></span><span class="pl-v" data-code-text="KEY"></span><span data-code-text=", "></span><span class="pl-v" data-code-text="CIPHER"></span><span data-code-text=", "></span><span class="pl-s1" data-code-text="type"></span><span class="pl-c1" data-code-text="="></span><span class="pl-s" data-code-text="&#39;hex&#39;"></span><span data-code-text="):"></span></div></div></div><div data-key="521" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10420px); min-height: auto;"><div><div id="LC522" class="react-file-line html-div" data-testid="code-cell" data-line-number="522" style="position: relative;"><span data-code-text="        "></span><span class="pl-k" data-code-text="if"></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="type"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="in"></span><span data-code-text=" ["></span><span class="pl-s" data-code-text="&#39;hex&#39;"></span><span data-code-text=", "></span><span class="pl-s" data-code-text="&#39;0b&#39;"></span><span data-code-text=", "></span><span class="pl-s" data-code-text="&#39;b64&#39;"></span><span data-code-text="]:"></span></div></div></div><div data-key="522" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10440px); min-height: auto;"><div><div id="LC523" class="react-file-line html-div" data-testid="code-cell" data-line-number="523" style="position: relative;"><span data-code-text="            "></span><span class="pl-s1" data-code-text="self"></span><span data-code-text="."></span><span class="pl-en" data-code-text="__keySchedule"></span><span data-code-text="("></span><span class="pl-v" data-code-text="KEY"></span><span data-code-text=")"></span></div></div></div><div data-key="523" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10460px); min-height: auto;"><div><div id="LC524" class="react-file-line html-div" data-testid="code-cell" data-line-number="524" style="position: relative;"><span data-code-text="            "></span><span class="pl-s1" data-code-text="data"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s" data-code-text="&#39;&#39;"></span></div></div></div><div data-key="524" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10480px); min-height: auto;"><div><div id="LC525" class="react-file-line html-div" data-testid="code-cell" data-line-number="525" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="525" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10500px); min-height: auto;"><div><div id="LC526" class="react-file-line html-div" data-testid="code-cell" data-line-number="526" style="position: relative;"><span data-code-text="            "></span><span class="pl-k" data-code-text="if"></span><span data-code-text=" ("></span><span class="pl-s1" data-code-text="type"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="=="></span><span data-code-text=" "></span><span class="pl-s" data-code-text="&#39;b64&#39;"></span><span data-code-text="):"></span></div></div></div><div data-key="526" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10520px); min-height: auto;"><div><div id="LC527" class="react-file-line html-div" data-testid="code-cell" data-line-number="527" style="position: relative;"><span data-code-text="                "></span><span class="pl-v" data-code-text="CIPHER"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-en" data-code-text="b64decode"></span><span data-code-text="("></span><span class="pl-v" data-code-text="CIPHER"></span><span data-code-text=")."></span><span class="pl-en" data-code-text="hex"></span><span data-code-text="()"></span></div></div></div><div data-key="527" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10540px); min-height: auto;"><div><div id="LC528" class="react-file-line html-div" data-testid="code-cell" data-line-number="528" style="position: relative;"><span data-code-text="                "></span><span class="pl-en" data-code-text="print"></span><span data-code-text="("></span><span class="pl-s" data-code-text="&quot;cipher in b64&quot;"></span><span data-code-text=","></span><span class="pl-v" data-code-text="CIPHER"></span><span data-code-text=")"></span></div></div></div><div data-key="528" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10560px); min-height: auto;"><div><div id="LC529" class="react-file-line html-div" data-testid="code-cell" data-line-number="529" style="position: relative;"><span data-code-text="            "></span><span class="pl-k" data-code-text="if"></span><span data-code-text=" ("></span><span class="pl-s1" data-code-text="type"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="=="></span><span data-code-text=" "></span><span class="pl-s" data-code-text="&#39;0b&#39;"></span><span data-code-text="):"></span></div></div></div><div data-key="529" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10580px); min-height: auto;"><div><div id="LC530" class="react-file-line html-div" data-testid="code-cell" data-line-number="530" style="position: relative;"><span data-code-text="                "></span><span class="pl-v" data-code-text="CIPHER"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-en" data-code-text="hex"></span><span data-code-text="("></span><span class="pl-en" data-code-text="int"></span><span data-code-text="("></span><span class="pl-v" data-code-text="CIPHER"></span><span data-code-text=", "></span><span class="pl-c1" data-code-text="2"></span><span data-code-text="))."></span><span class="pl-en" data-code-text="replace"></span><span data-code-text="("></span><span class="pl-s" data-code-text="&#39;0x&#39;"></span><span data-code-text=", "></span><span class="pl-s" data-code-text="&#39;&#39;"></span><span data-code-text=")"></span></div></div></div><div data-key="530" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10600px); min-height: auto;"><div><div id="LC531" class="react-file-line html-div" data-testid="code-cell" data-line-number="531" style="position: relative;"><span data-code-text="                "></span><span class="pl-en" data-code-text="print"></span><span data-code-text="("></span><span class="pl-s" data-code-text="&quot;cipher in 0b&quot;"></span><span data-code-text=","></span><span class="pl-v" data-code-text="CIPHER"></span><span data-code-text=")"></span></div></div></div><div data-key="531" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10620px); min-height: auto;"><div><div id="LC532" class="react-file-line html-div" data-testid="code-cell" data-line-number="532" style="position: relative;"><span data-code-text="            "></span><span class="pl-k" data-code-text="if"></span><span data-code-text=" ("></span><span class="pl-en" data-code-text="len"></span><span data-code-text="("></span><span class="pl-v" data-code-text="CIPHER"></span><span data-code-text=") "></span><span class="pl-c1" data-code-text="%"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="32"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="=="></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="0"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="and"></span><span data-code-text=" "></span><span class="pl-en" data-code-text="len"></span><span data-code-text="("></span><span class="pl-v" data-code-text="CIPHER"></span><span data-code-text=") "></span><span class="pl-c1" data-code-text="&gt;"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="0"></span><span data-code-text="):"></span></div></div></div><div data-key="532" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10640px); min-height: auto;"><div><div id="LC533" class="react-file-line html-div" data-testid="code-cell" data-line-number="533" style="position: relative;"><span data-code-text="                "></span><span class="pl-s1" data-code-text="examine"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-v" data-code-text="CIPHER"></span></div></div></div><div data-key="533" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10660px); min-height: auto;"><div><div id="LC534" class="react-file-line html-div" data-testid="code-cell" data-line-number="534" style="position: relative;"><span data-code-text="                "></span><span class="pl-k" data-code-text="while"></span><span data-code-text=" ("></span><span class="pl-en" data-code-text="len"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="examine"></span><span data-code-text=") "></span><span class="pl-c1" data-code-text="!="></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="0"></span><span data-code-text="):"></span></div></div></div><div data-key="534" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10680px); min-height: auto;"><div><div id="LC535" class="react-file-line html-div" data-testid="code-cell" data-line-number="535" style="position: relative;"><span data-code-text="                    "></span><span class="pl-s1" data-code-text="plain_matrix"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="self"></span><span data-code-text="."></span><span class="pl-en" data-code-text="__decryptProcess"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="examine"></span><span data-code-text="[:"></span><span class="pl-c1" data-code-text="32"></span><span data-code-text="])"></span></div></div></div><div data-key="535" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10700px); min-height: auto;"><div><div id="LC536" class="react-file-line html-div" data-testid="code-cell" data-line-number="536" style="position: relative;"><span data-code-text="                    "></span><span class="pl-s1" data-code-text="plain_arr"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-en" data-code-text="list"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="np"></span><span data-code-text="."></span><span class="pl-en" data-code-text="array"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="plain_matrix"></span><span data-code-text=")."></span><span class="pl-en" data-code-text="reshape"></span><span data-code-text="("></span><span class="pl-c1" data-code-text="-"></span><span class="pl-c1" data-code-text="1"></span><span data-code-text=", ))"></span></div></div></div><div data-key="536" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10720px); min-height: auto;"><div><div id="LC537" class="react-file-line html-div" data-testid="code-cell" data-line-number="537" style="position: relative;"><span data-code-text="                    "></span><span class="pl-s1" data-code-text="plain_arr"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="self"></span><span data-code-text="."></span><span class="pl-en" data-code-text="__delPadding"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="plain_arr"></span><span data-code-text=")"></span></div></div></div><div data-key="537" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10740px); min-height: auto;"><div><div id="LC538" class="react-file-line html-div" data-testid="code-cell" data-line-number="538" style="position: relative;"><span data-code-text="                    "></span><span class="pl-k" data-code-text="for"></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="j"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="in"></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="plain_arr"></span><span data-code-text=":"></span></div></div></div><div data-key="538" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10760px); min-height: auto;"><div><div id="LC539" class="react-file-line html-div" data-testid="code-cell" data-line-number="539" style="position: relative;"><span data-code-text="                        "></span><span class="pl-s1" data-code-text="data"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="+="></span><span data-code-text=" "></span><span class="pl-en" data-code-text="chr"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="j"></span><span data-code-text=")"></span></div></div></div><div data-key="539" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10780px); min-height: auto;"><div><div id="LC540" class="react-file-line html-div" data-testid="code-cell" data-line-number="540" style="position: relative;"><span data-code-text="                    "></span><span class="pl-k" data-code-text="if"></span><span data-code-text=" ("></span><span class="pl-en" data-code-text="len"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="examine"></span><span data-code-text=") "></span><span class="pl-c1" data-code-text="=="></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="32"></span><span data-code-text="):"></span></div></div></div><div data-key="540" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10800px); min-height: auto;"><div><div id="LC541" class="react-file-line html-div" data-testid="code-cell" data-line-number="541" style="position: relative;"><span data-code-text="                        "></span><span class="pl-s1" data-code-text="examine"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s" data-code-text="&#39;&#39;"></span></div></div></div><div data-key="541" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10820px); min-height: auto;"><div><div id="LC542" class="react-file-line html-div" data-testid="code-cell" data-line-number="542" style="position: relative;"><span data-code-text="                    "></span><span class="pl-k" data-code-text="else"></span><span data-code-text=":"></span></div></div></div><div data-key="542" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10840px); min-height: auto;"><div><div id="LC543" class="react-file-line html-div" data-testid="code-cell" data-line-number="543" style="position: relative;"><span data-code-text="                        "></span><span class="pl-s1" data-code-text="examine"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="examine"></span><span data-code-text="["></span><span class="pl-c1" data-code-text="32"></span><span data-code-text=":]"></span></div></div></div><div data-key="543" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10860px); min-height: auto;"><div><div id="LC544" class="react-file-line html-div" data-testid="code-cell" data-line-number="544" style="position: relative;"><span data-code-text="                "></span><span class="pl-s1" data-code-text="self"></span><span data-code-text="."></span><span class="pl-v" data-code-text="ROUNDKEY"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" []"></span></div></div></div><div data-key="544" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10880px); min-height: auto;"><div><div id="LC545" class="react-file-line html-div" data-testid="code-cell" data-line-number="545" style="position: relative;"><span data-code-text="                "></span><span class="pl-k" data-code-text="return"></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="data"></span></div></div></div><div data-key="545" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10900px); min-height: auto;"><div><div id="LC546" class="react-file-line html-div" data-testid="code-cell" data-line-number="546" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="546" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10920px); min-height: auto;"><div><div id="LC547" class="react-file-line html-div" data-testid="code-cell" data-line-number="547" style="position: relative;"><span data-code-text="            "></span><span class="pl-k" data-code-text="else"></span><span data-code-text=":"></span></div></div></div><div data-key="547" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10940px); min-height: auto;"><div><div id="LC548" class="react-file-line html-div" data-testid="code-cell" data-line-number="548" style="position: relative;"><span data-code-text="                "></span><span class="pl-k" data-code-text="raise"></span><span data-code-text=" "></span><span class="pl-v" data-code-text="Exception"></span><span data-code-text="("></span><span class="pl-s"><span data-code-text="f&quot;Hex: "></span><span class="pl-s1"><span class="pl-kos" data-code-text="{"></span><span class="pl-v" data-code-text="CIPHER"></span><span class="pl-kos" data-code-text="}"></span></span><span data-code-text=", should be non-empty multiple of 32bits&quot;"></span></span><span data-code-text=")"></span></div></div></div><div data-key="548" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10960px); min-height: auto;"><div><div id="LC549" class="react-file-line html-div" data-testid="code-cell" data-line-number="549" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="549" class="child-of-line-390 child-of-line-521  react-code-text react-code-line-contents virtual" style="transform: translateY(10980px); min-height: auto;"><div><div id="LC550" class="react-file-line html-div" data-testid="code-cell" data-line-number="550" style="position: relative;"><span data-code-text="        "></span><span class="pl-k" data-code-text="else"></span><span data-code-text=":"></span></div></div></div><div data-key="550" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11000px); min-height: auto;"><div><div id="LC551" class="react-file-line html-div" data-testid="code-cell" data-line-number="551" style="position: relative;"><span data-code-text="            "></span><span class="pl-k" data-code-text="raise"></span><span data-code-text=" "></span><span class="pl-v" data-code-text="Exception"></span><span data-code-text="("></span><span class="pl-s"><span data-code-text="f&quot;type := [&#39;hex&#39;, &#39;0b&#39;, &#39;b64&#39;] but got &#39;"></span><span class="pl-s1"><span class="pl-kos" data-code-text="{"></span><span class="pl-s1" data-code-text="type"></span><span class="pl-kos" data-code-text="}"></span></span><span data-code-text="&#39;&quot;"></span></span><span data-code-text=")"></span></div></div></div><div data-key="551" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11020px); min-height: auto;"><div><div id="LC552" class="react-file-line html-div" data-testid="code-cell" data-line-number="552" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="552" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11040px); min-height: auto;"><div><div id="LC553" class="react-file-line html-div" data-testid="code-cell" data-line-number="553" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="553" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11060px); min-height: auto;"><div><div id="LC554" class="react-file-line html-div" data-testid="code-cell" data-line-number="554" style="position: relative;"><span class="pl-k" data-code-text="if"></span><span data-code-text=" ("></span><span class="pl-s1" data-code-text="__name__"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="=="></span><span data-code-text=" "></span><span class="pl-s" data-code-text="&#39;__main__&#39;"></span><span data-code-text="):"></span></div></div></div><div data-key="554" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11080px); min-height: auto;"><div><div id="LC555" class="react-file-line html-div" data-testid="code-cell" data-line-number="555" style="position: relative;"><span data-code-text="    "></span><span class="pl-s1" data-code-text="aes256"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-v" data-code-text="AES"></span><span data-code-text="()"></span></div></div></div><div data-key="555" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11100px); min-height: auto;"><div><div id="LC556" class="react-file-line html-div" data-testid="code-cell" data-line-number="556" style="position: relative;"><span data-code-text="    "></span><span class="pl-s1" data-code-text="key"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s" data-code-text="&#39;Thats my Kung Fu1234567876543210&#39;"></span></div></div></div><div data-key="556" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11120px); min-height: auto;"><div><div id="LC557" class="react-file-line html-div" data-testid="code-cell" data-line-number="557" style="position: relative;"><span data-code-text="    "></span><span class="pl-en" data-code-text="print"></span><span data-code-text="("></span><span class="pl-s" data-code-text="&quot;***************************************&quot;"></span><span data-code-text=")"></span></div></div></div><div data-key="557" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11140px); min-height: auto;"><div><div id="LC558" class="react-file-line html-div" data-testid="code-cell" data-line-number="558" style="position: relative;"><span data-code-text="    "></span><span class="pl-s1" data-code-text="filenameencypt"></span><span class="pl-c1" data-code-text="="></span><span class="pl-en" data-code-text="input"></span><span data-code-text="("></span><span class="pl-s" data-code-text="&quot;enter file name to encryption &quot;"></span><span data-code-text=")"></span><span class="pl-c1" data-code-text="+"></span><span class="pl-s" data-code-text="&quot;.pdf&quot;"></span></div></div></div><div data-key="558" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11160px); min-height: auto;"><div><div id="LC559" class="react-file-line html-div" data-testid="code-cell" data-line-number="559" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="559" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11180px); min-height: auto;"><div><div id="LC560" class="react-file-line html-div" data-testid="code-cell" data-line-number="560" style="position: relative;"><span data-code-text="    "></span><span class="pl-k" data-code-text="with"></span><span data-code-text=" "></span><span class="pl-en" data-code-text="open"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="filenameencypt"></span><span data-code-text=", "></span><span class="pl-s" data-code-text="&quot;rb&quot;"></span><span data-code-text=") "></span><span class="pl-k" data-code-text="as"></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="pdf_file"></span><span data-code-text=":"></span></div></div></div><div data-key="560" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11200px); min-height: auto;"><div><div id="LC561" class="react-file-line html-div" data-testid="code-cell" data-line-number="561" style="position: relative;"><span data-code-text="        "></span><span class="pl-s1" data-code-text="encoded"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="base64"></span><span data-code-text="."></span><span class="pl-en" data-code-text="b64encode"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="pdf_file"></span><span data-code-text="."></span><span class="pl-en" data-code-text="read"></span><span data-code-text="())"></span></div></div></div><div data-key="561" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11220px); min-height: auto;"><div><div id="LC562" class="react-file-line html-div" data-testid="code-cell" data-line-number="562" style="position: relative;"><span data-code-text="        "></span><span class="pl-s1" data-code-text="encoded_string"></span><span class="pl-c1" data-code-text="="></span><span class="pl-s1" data-code-text="encoded"></span><span data-code-text="."></span><span class="pl-en" data-code-text="decode"></span><span data-code-text="("></span><span class="pl-s" data-code-text="&#39;utf-8&#39;"></span><span data-code-text=")"></span></div></div></div><div data-key="562" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11240px); min-height: auto;"><div><div id="LC563" class="react-file-line html-div" data-testid="code-cell" data-line-number="563" style="position: relative;"><span data-code-text="    "></span><span class="pl-s1" data-code-text="stretime"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="datetime"></span><span data-code-text="."></span><span class="pl-s1" data-code-text="datetime"></span><span data-code-text="."></span><span class="pl-en" data-code-text="now"></span><span data-code-text="()"></span></div></div></div><div data-key="563" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11260px); min-height: auto;"><div><div id="LC564" class="react-file-line html-div" data-testid="code-cell" data-line-number="564" style="position: relative;"><span data-code-text="    "></span><span class="pl-s1" data-code-text="c"></span><span class="pl-c1" data-code-text="="></span><span data-code-text="("></span><span class="pl-s1" data-code-text="aes256"></span><span data-code-text="."></span><span class="pl-en" data-code-text="encrypt"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="key"></span><span data-code-text=","></span><span class="pl-s1" data-code-text="encoded_string"></span><span data-code-text=","></span><span class="pl-s" data-code-text="&#39;0b&#39;"></span><span data-code-text="))"></span></div></div></div><div data-key="564" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11280px); min-height: auto;"><div><div id="LC565" class="react-file-line html-div" data-testid="code-cell" data-line-number="565" style="position: relative;"><span data-code-text="    "></span><span class="pl-s1" data-code-text="endetime"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="datetime"></span><span data-code-text="."></span><span class="pl-s1" data-code-text="datetime"></span><span data-code-text="."></span><span class="pl-en" data-code-text="now"></span><span data-code-text="()"></span></div></div></div><div data-key="565" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11300px); min-height: auto;"><div><div id="LC566" class="react-file-line html-div" data-testid="code-cell" data-line-number="566" style="position: relative;"><span data-code-text="    "></span><span class="pl-en" data-code-text="print"></span><span data-code-text="("></span><span class="pl-s" data-code-text="&quot;encryption takes &quot;"></span><span data-code-text=", ("></span><span class="pl-s1" data-code-text="endetime"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="-"></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="stretime"></span><span data-code-text=")."></span><span class="pl-s1" data-code-text="microseconds"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="*"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="1000"></span><span data-code-text=", "></span><span class="pl-s" data-code-text="&quot; milli seconds&quot;"></span><span data-code-text=")"></span></div></div></div><div data-key="566" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11320px); min-height: auto;"><div><div id="LC567" class="react-file-line html-div" data-testid="code-cell" data-line-number="567" style="position: relative;"><span data-code-text="    "></span><span class="pl-s1" data-code-text="file_64_decodee10"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="base64"></span><span data-code-text="."></span><span class="pl-en" data-code-text="b64decode"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="c"></span><span data-code-text=")"></span></div></div></div><div data-key="567" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11340px); min-height: auto;"><div><div id="LC568" class="react-file-line html-div" data-testid="code-cell" data-line-number="568" style="position: relative;"><span data-code-text="    "></span><span class="pl-s1" data-code-text="file_resultc"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-en" data-code-text="open"></span><span data-code-text="("></span><span class="pl-s" data-code-text="&#39;encryption file.pdf&#39;"></span><span data-code-text=", "></span><span class="pl-s" data-code-text="&#39;wb&#39;"></span><span data-code-text=")"></span></div></div></div><div data-key="568" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11360px); min-height: auto;"><div><div id="LC569" class="react-file-line html-div" data-testid="code-cell" data-line-number="569" style="position: relative;"><span data-code-text="    "></span><span class="pl-s1" data-code-text="file_resultc"></span><span data-code-text="."></span><span class="pl-en" data-code-text="write"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="file_64_decodee10"></span><span data-code-text=")"></span></div></div></div><div data-key="569" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11380px); min-height: auto;"><div><div id="LC570" class="react-file-line html-div" data-testid="code-cell" data-line-number="570" style="position: relative;"><span data-code-text="    "></span><span class="pl-en" data-code-text="print"></span><span data-code-text="("></span><span class="pl-s" data-code-text="&quot;encryption done with encryption file&quot;"></span><span data-code-text=")"></span></div></div></div><div data-key="570" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11400px); min-height: auto;"><div><div id="LC571" class="react-file-line html-div" data-testid="code-cell" data-line-number="571" style="position: relative;"><span data-code-text="
"></span></div></div></div><div data-key="571" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11420px); min-height: auto;"><div><div id="LC572" class="react-file-line html-div" data-testid="code-cell" data-line-number="572" style="position: relative;"><span data-code-text="    "></span><span class="pl-en" data-code-text="print"></span><span data-code-text="("></span><span class="pl-s" data-code-text="&quot;***************************************&quot;"></span><span data-code-text=")"></span></div></div></div><div data-key="572" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11440px); min-height: auto;"><div><div id="LC573" class="react-file-line html-div" data-testid="code-cell" data-line-number="573" style="position: relative;"><span data-code-text="    "></span><span class="pl-s1" data-code-text="filenamedecrypt"></span><span class="pl-c1" data-code-text="="></span><span class="pl-en" data-code-text="input"></span><span data-code-text="("></span><span class="pl-s" data-code-text="&quot;enter file to decryption&quot;"></span><span data-code-text=")"></span><span class="pl-c1" data-code-text="+"></span><span class="pl-s" data-code-text="&quot;.pdf&quot;"></span></div></div></div><div data-key="573" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11460px); min-height: auto;"><div><div id="LC574" class="react-file-line html-div" data-testid="code-cell" data-line-number="574" style="position: relative;"><span data-code-text="    "></span><span class="pl-k" data-code-text="with"></span><span data-code-text=" "></span><span class="pl-en" data-code-text="open"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="filenamedecrypt"></span><span data-code-text=", "></span><span class="pl-s" data-code-text="&quot;rb&quot;"></span><span data-code-text=") "></span><span class="pl-k" data-code-text="as"></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="pdf_file"></span><span data-code-text=":"></span></div></div></div><div data-key="574" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11480px); min-height: auto;"><div><div id="LC575" class="react-file-line html-div" data-testid="code-cell" data-line-number="575" style="position: relative;"><span data-code-text="        "></span><span class="pl-s1" data-code-text="cc"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="base64"></span><span data-code-text="."></span><span class="pl-en" data-code-text="b64encode"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="pdf_file"></span><span data-code-text="."></span><span class="pl-en" data-code-text="read"></span><span data-code-text="())"></span></div></div></div><div data-key="575" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11500px); min-height: auto;"><div><div id="LC576" class="react-file-line html-div" data-testid="code-cell" data-line-number="576" style="position: relative;"><span data-code-text="    "></span><span class="pl-s1" data-code-text="strtimdec"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="datetime"></span><span data-code-text="."></span><span class="pl-s1" data-code-text="datetime"></span><span data-code-text="."></span><span class="pl-en" data-code-text="now"></span><span data-code-text="()"></span></div></div></div><div data-key="576" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11520px); min-height: auto;"><div><div id="LC577" class="react-file-line html-div" data-testid="code-cell" data-line-number="577" style="position: relative;"><span data-code-text="    "></span><span class="pl-s1" data-code-text="m"></span><span class="pl-c1" data-code-text="="></span><span class="pl-s1" data-code-text="aes256"></span><span data-code-text="."></span><span class="pl-en" data-code-text="decrypt"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="key"></span><span data-code-text=","></span><span class="pl-s1" data-code-text="cc"></span><span data-code-text=","></span><span class="pl-s" data-code-text="&#39;0b&#39;"></span><span data-code-text=")"></span></div></div></div><div data-key="577" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11540px); min-height: auto;"><div><div id="LC578" class="react-file-line html-div" data-testid="code-cell" data-line-number="578" style="position: relative;"><span data-code-text="    "></span><span class="pl-s1" data-code-text="endetimdec"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="datetime"></span><span data-code-text="."></span><span class="pl-s1" data-code-text="datetime"></span><span data-code-text="."></span><span class="pl-en" data-code-text="now"></span><span data-code-text="()"></span></div></div></div><div data-key="578" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11560px); min-height: auto;"><div><div id="LC579" class="react-file-line html-div" data-testid="code-cell" data-line-number="579" style="position: relative;"><span data-code-text="    "></span><span class="pl-en" data-code-text="print"></span><span data-code-text="("></span><span class="pl-s" data-code-text="&quot;encryption takes &quot;"></span><span data-code-text=", ("></span><span class="pl-s1" data-code-text="endetimdec"></span><span class="pl-c1" data-code-text="-"></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="strtimdec"></span><span data-code-text=")."></span><span class="pl-s1" data-code-text="microseconds"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="*"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="1000"></span><span data-code-text=", "></span><span class="pl-s" data-code-text="&quot; milli seconds&quot;"></span><span data-code-text=")"></span></div></div></div><div data-key="579" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11580px); min-height: auto;"><div><div id="LC580" class="react-file-line html-div" data-testid="code-cell" data-line-number="580" style="position: relative;"><span data-code-text="    "></span><span class="pl-s1" data-code-text="file_64_decoded00"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-s1" data-code-text="base64"></span><span data-code-text="."></span><span class="pl-en" data-code-text="b64decode"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="m"></span><span data-code-text=")"></span></div></div></div><div data-key="580" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11600px); min-height: auto;"><div><div id="LC581" class="react-file-line html-div" data-testid="code-cell" data-line-number="581" style="position: relative;"><span data-code-text="    "></span><span class="pl-s1" data-code-text="file_result00"></span><span data-code-text=" "></span><span class="pl-c1" data-code-text="="></span><span data-code-text=" "></span><span class="pl-en" data-code-text="open"></span><span data-code-text="("></span><span class="pl-s" data-code-text="&#39;decryption file.pdf&#39;"></span><span data-code-text=", "></span><span class="pl-s" data-code-text="&#39;wb&#39;"></span><span data-code-text=")"></span></div></div></div><div data-key="581" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11620px); min-height: auto;"><div><div id="LC582" class="react-file-line html-div" data-testid="code-cell" data-line-number="582" style="position: relative;"><span data-code-text="    "></span><span class="pl-s1" data-code-text="file_result00"></span><span data-code-text="."></span><span class="pl-en" data-code-text="write"></span><span data-code-text="("></span><span class="pl-s1" data-code-text="file_64_decoded00"></span><span data-code-text=")"></span></div></div></div><div data-key="582" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11640px); min-height: auto;"><div><div id="LC583" class="react-file-line html-div" data-testid="code-cell" data-line-number="583" style="position: relative;"><span data-code-text="    "></span><span class="pl-en" data-code-text="print"></span><span data-code-text="("></span><span class="pl-s" data-code-text="&quot;***************************************&quot;"></span><span data-code-text=")"></span></div></div></div><div data-key="583" class="react-code-text react-code-line-contents virtual" style="transform: translateY(11660px); min-height: auto;"><div><div id="LC584" class="react-file-line html-div" data-testid="code-cell" data-line-number="584" style="position: relative;"><span data-code-text="    "></span><span class="pl-en" data-code-text="print"></span><span data-code-text="("></span><span class="pl-s" data-code-text="&quot;decryption done with decryption file&quot;"></span><span data-code-text=")"></span></div></div></div></div><button hidden="" data-hotkey="Control+a"></button><div aria-hidden="true" data-testid="navigation-cursor" class="Box-sc-g0xbh4-0 code-navigation-cursor" style="top: 0px; left: 92px;"> </div><button hidden="" data-testid="NavigationCursorEnter" data-hotkey="Control+Enter" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorSetHighlightedLine" data-hotkey="Shift+J" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorSetHighlightAndExpandMenu" data-hotkey="Alt+Shift+C,Alt+Shift+Ç" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorPageDown" data-hotkey="PageDown" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorPageUp" data-hotkey="PageUp" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="" data-hotkey="/" data-hotkey-scope="read-only-cursor-text-area"></button></div></div></div></div><div id="copilot-button-container"></div></div><div id="highlighted-line-menu-container"></div></div></div></section></div></div><div class="Box-sc-g0xbh4-0 ktQnIo"></div><div class="Box-sc-g0xbh4-0 eytzQM panel-content-narrow-styles inner-panel-content-not-narrow"><div id="symbols-pane" class="Box-sc-g0xbh4-0"><div aria-labelledby="symbols-pane-header" class="Box-sc-g0xbh4-0 bJNAmt"><div class="Box-sc-g0xbh4-0 ipXucK"><h2 id="symbols-pane-header" tabindex="-1" class="Box-sc-g0xbh4-0 wMEyi">Symbols</h2><button data-component="IconButton" type="button" aria-label="Close symbols" data-hotkey="Escape" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 eyqOHf"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-x" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path></svg></button></div><div class="Box-sc-g0xbh4-0 fHqdLt">Find definitions and references for functions and other symbols in this file by clicking a symbol below or in the code.</div><span class="TextInputWrapper__TextInputBaseWrapper-sc-1mqhpbi-0 TextInputWrapper-sc-1mqhpbi-1 leBhzd dWJhEx TextInput-wrapper" aria-busy="false"><span class="TextInput-icon"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M.75 3h14.5a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1 0-1.5ZM3 7.75A.75.75 0 0 1 3.75 7h8.5a.75.75 0 0 1 0 1.5h-8.5A.75.75 0 0 1 3 7.75Zm3 4a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 0 1.5h-2.5a.75.75 0 0 1-.75-.75Z"></path></svg></span><input type="text" placeholder="Filter symbols" name="Filter symbols" aria-label="Filter symbols" aria-controls="filter-results" aria-expanded="true" aria-autocomplete="list" role="combobox" data-component="input" class="UnstyledTextInput-sc-14ypya-0 cDLBls" value=""><span class="TextInput-icon"><div class="Box-sc-g0xbh4-0 ckwgci"><kbd>r</kbd></div></span></span><div class="Box-sc-g0xbh4-0 jGYebd"><div id="filter-results" class="Box-sc-g0xbh4-0 kgNotW"><span role="status" aria-live="polite" aria-atomic="true" class="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0 rTZSs"></span><ul role="tree" aria-label="Code Navigation" data-omit-spacer="false" class="TreeView__UlBox-sc-4ex6b6-0 dcpVHE"><li class="PRIVATE_TreeView-item" tabindex="0" id="0roundConstant" role="treeitem" aria-labelledby=":Rq6naladaj5:" aria-describedby=":Rq6naladaj5H1: :Rq6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rq6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 hKxYar"></div><div class="Box-sc-g0xbh4-0 gjBYJx">const</div></div>  <div title="roundConstant" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">roundConstant</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="1roundConstant_8" role="treeitem" aria-labelledby=":R1a6naladaj5:" aria-describedby=":R1a6naladaj5H1: :R1a6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R1a6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 hKxYar"></div><div class="Box-sc-g0xbh4-0 gjBYJx">const</div></div>  <div title="roundConstant_8" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">roundConstant_8</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="2s_box" role="treeitem" aria-labelledby=":R1q6naladaj5:" aria-describedby=":R1q6naladaj5H1: :R1q6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R1q6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 hKxYar"></div><div class="Box-sc-g0xbh4-0 gjBYJx">const</div></div>  <div title="s_box" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">s_box</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="3invs_box" role="treeitem" aria-labelledby=":R2a6naladaj5:" aria-describedby=":R2a6naladaj5H1: :R2a6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R2a6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 hKxYar"></div><div class="Box-sc-g0xbh4-0 gjBYJx">const</div></div>  <div title="invs_box" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">invs_box</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="4encryptMDS" role="treeitem" aria-labelledby=":R2q6naladaj5:" aria-describedby=":R2q6naladaj5H1: :R2q6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R2q6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 hKxYar"></div><div class="Box-sc-g0xbh4-0 gjBYJx">const</div></div>  <div title="encryptMDS" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">encryptMDS</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="5encryptMDS_8" role="treeitem" aria-labelledby=":R3a6naladaj5:" aria-describedby=":R3a6naladaj5H1: :R3a6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R3a6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 hKxYar"></div><div class="Box-sc-g0xbh4-0 gjBYJx">const</div></div>  <div title="encryptMDS_8" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">encryptMDS_8</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="6decryptMDS" role="treeitem" aria-labelledby=":R3q6naladaj5:" aria-describedby=":R3q6naladaj5H1: :R3q6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R3q6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 hKxYar"></div><div class="Box-sc-g0xbh4-0 gjBYJx">const</div></div>  <div title="decryptMDS" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">decryptMDS</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="7decryptMDS_8" role="treeitem" aria-labelledby=":R4a6naladaj5:" aria-describedby=":R4a6naladaj5H1: :R4a6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R4a6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 hKxYar"></div><div class="Box-sc-g0xbh4-0 gjBYJx">const</div></div>  <div title="decryptMDS_8" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">decryptMDS_8</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="8mc2" role="treeitem" aria-labelledby=":R4q6naladaj5:" aria-describedby=":R4q6naladaj5H1: :R4q6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R4q6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 hKxYar"></div><div class="Box-sc-g0xbh4-0 gjBYJx">const</div></div>  <div title="mc2" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">mc2</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="9mc3" role="treeitem" aria-labelledby=":R5a6naladaj5:" aria-describedby=":R5a6naladaj5H1: :R5a6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R5a6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 hKxYar"></div><div class="Box-sc-g0xbh4-0 gjBYJx">const</div></div>  <div title="mc3" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">mc3</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="10mc9" role="treeitem" aria-labelledby=":R5q6naladaj5:" aria-describedby=":R5q6naladaj5H1: :R5q6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R5q6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 hKxYar"></div><div class="Box-sc-g0xbh4-0 gjBYJx">const</div></div>  <div title="mc9" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">mc9</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="11mc11" role="treeitem" aria-labelledby=":R6a6naladaj5:" aria-describedby=":R6a6naladaj5H1: :R6a6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R6a6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 hKxYar"></div><div class="Box-sc-g0xbh4-0 gjBYJx">const</div></div>  <div title="mc11" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">mc11</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="12mc13" role="treeitem" aria-labelledby=":R6q6naladaj5:" aria-describedby=":R6q6naladaj5H1: :R6q6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R6q6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 hKxYar"></div><div class="Box-sc-g0xbh4-0 gjBYJx">const</div></div>  <div title="mc13" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">mc13</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="13mc14" role="treeitem" aria-labelledby=":R7a6naladaj5:" aria-describedby=":R7a6naladaj5H1: :R7a6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R7a6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 hKxYar"></div><div class="Box-sc-g0xbh4-0 gjBYJx">const</div></div>  <div title="mc14" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">mc14</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="14keyToHexArray" role="treeitem" aria-labelledby=":R7q6naladaj5:" aria-describedby=":R7q6naladaj5H1: :R7q6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R7q6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 cDCIeg"></div><div class="Box-sc-g0xbh4-0 dIEiEC">func</div></div>  <div title="keyToHexArray" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">keyToHexArray</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="15arrayShift" role="treeitem" aria-labelledby=":R8a6naladaj5:" aria-describedby=":R8a6naladaj5H1: :R8a6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R8a6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 cDCIeg"></div><div class="Box-sc-g0xbh4-0 dIEiEC">func</div></div>  <div title="arrayShift" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">arrayShift</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="16arraySbox" role="treeitem" aria-labelledby=":R8q6naladaj5:" aria-describedby=":R8q6naladaj5H1: :R8q6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R8q6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 cDCIeg"></div><div class="Box-sc-g0xbh4-0 dIEiEC">func</div></div>  <div title="arraySbox" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">arraySbox</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="17arrayInvSbox" role="treeitem" aria-labelledby=":R9a6naladaj5:" aria-describedby=":R9a6naladaj5H1: :R9a6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R9a6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 cDCIeg"></div><div class="Box-sc-g0xbh4-0 dIEiEC">func</div></div>  <div title="arrayInvSbox" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">arrayInvSbox</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="18xorArray" role="treeitem" aria-labelledby=":R9q6naladaj5:" aria-describedby=":R9q6naladaj5H1: :R9q6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R9q6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 cDCIeg"></div><div class="Box-sc-g0xbh4-0 dIEiEC">func</div></div>  <div title="xorArray" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">xorArray</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="19addRoundKey" role="treeitem" aria-labelledby=":Raa6naladaj5:" aria-describedby=":Raa6naladaj5H1: :Raa6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Raa6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 cDCIeg"></div><div class="Box-sc-g0xbh4-0 dIEiEC">func</div></div>  <div title="addRoundKey" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">addRoundKey</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="20subBytes" role="treeitem" aria-labelledby=":Raq6naladaj5:" aria-describedby=":Raq6naladaj5H1: :Raq6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Raq6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 cDCIeg"></div><div class="Box-sc-g0xbh4-0 dIEiEC">func</div></div>  <div title="subBytes" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">subBytes</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="21shiftRow" role="treeitem" aria-labelledby=":Rba6naladaj5:" aria-describedby=":Rba6naladaj5H1: :Rba6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rba6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 cDCIeg"></div><div class="Box-sc-g0xbh4-0 dIEiEC">func</div></div>  <div title="shiftRow" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">shiftRow</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="22mixColumn" role="treeitem" aria-labelledby=":Rbq6naladaj5:" aria-describedby=":Rbq6naladaj5H1: :Rbq6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rbq6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 cDCIeg"></div><div class="Box-sc-g0xbh4-0 dIEiEC">func</div></div>  <div title="mixColumn" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">mixColumn</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="23inverseMixColumn" role="treeitem" aria-labelledby=":Rca6naladaj5:" aria-describedby=":Rca6naladaj5H1: :Rca6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rca6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 cDCIeg"></div><div class="Box-sc-g0xbh4-0 dIEiEC">func</div></div>  <div title="inverseMixColumn" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">inverseMixColumn</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="24hexToMatrix" role="treeitem" aria-labelledby=":Rcq6naladaj5:" aria-describedby=":Rcq6naladaj5H1: :Rcq6naladaj5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rcq6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 cDCIeg"></div><div class="Box-sc-g0xbh4-0 dIEiEC">func</div></div>  <div title="hexToMatrix" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">hexToMatrix</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="25AES" role="treeitem" aria-labelledby=":Rda6naladaj5:" aria-describedby=":Rda6naladaj5H1: :Rda6naladaj5H2:" aria-level="1" aria-expanded="true" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-chevron-down" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M6 8.825c-.2 0-.4-.1-.5-.2l-3.3-3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l2.7 2.7 2.7-2.7c.3-.3.8-.3 1.1 0 .3.3.3.8 0 1.1l-3.2 3.2c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":Rda6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 ixaBsj"></div><div class="Box-sc-g0xbh4-0 fBryRh">class</div></div>  <div title="AES" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">AES</span></div></div></span></div></div><ul role="group" style="list-style:none;padding:0;margin:0"><li class="PRIVATE_TreeView-item" tabindex="-1" id="0__init__" role="treeitem" aria-labelledby=":R6ta6naladaj5:" aria-describedby=":R6ta6naladaj5H1: :R6ta6naladaj5H2:" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:2"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"><div class="PRIVATE_TreeView-item-level-line"></div></div></div><div id=":R6ta6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 cDCIeg"></div><div class="Box-sc-g0xbh4-0 dIEiEC">func</div></div>  <div title="__init__" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">__init__</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="1__keySchedule" role="treeitem" aria-labelledby=":Rata6naladaj5:" aria-describedby=":Rata6naladaj5H1: :Rata6naladaj5H2:" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:2"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"><div class="PRIVATE_TreeView-item-level-line"></div></div></div><div id=":Rata6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 cDCIeg"></div><div class="Box-sc-g0xbh4-0 dIEiEC">func</div></div>  <div title="__keySchedule" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">__keySchedule</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="2__convertRoundKey" role="treeitem" aria-labelledby=":Reta6naladaj5:" aria-describedby=":Reta6naladaj5H1: :Reta6naladaj5H2:" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:2"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"><div class="PRIVATE_TreeView-item-level-line"></div></div></div><div id=":Reta6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 cDCIeg"></div><div class="Box-sc-g0xbh4-0 dIEiEC">func</div></div>  <div title="__convertRoundKey" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">__convertRoundKey</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="3__encryptProcess" role="treeitem" aria-labelledby=":Rita6naladaj5:" aria-describedby=":Rita6naladaj5H1: :Rita6naladaj5H2:" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:2"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"><div class="PRIVATE_TreeView-item-level-line"></div></div></div><div id=":Rita6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 cDCIeg"></div><div class="Box-sc-g0xbh4-0 dIEiEC">func</div></div>  <div title="__encryptProcess" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">__encryptProcess</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="4__addPadding" role="treeitem" aria-labelledby=":Rmta6naladaj5:" aria-describedby=":Rmta6naladaj5H1: :Rmta6naladaj5H2:" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:2"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"><div class="PRIVATE_TreeView-item-level-line"></div></div></div><div id=":Rmta6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 cDCIeg"></div><div class="Box-sc-g0xbh4-0 dIEiEC">func</div></div>  <div title="__addPadding" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">__addPadding</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="5__decryptProcess" role="treeitem" aria-labelledby=":Rqta6naladaj5:" aria-describedby=":Rqta6naladaj5H1: :Rqta6naladaj5H2:" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:2"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"><div class="PRIVATE_TreeView-item-level-line"></div></div></div><div id=":Rqta6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 cDCIeg"></div><div class="Box-sc-g0xbh4-0 dIEiEC">func</div></div>  <div title="__decryptProcess" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">__decryptProcess</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="6__delPadding" role="treeitem" aria-labelledby=":Ruta6naladaj5:" aria-describedby=":Ruta6naladaj5H1: :Ruta6naladaj5H2:" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:2"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"><div class="PRIVATE_TreeView-item-level-line"></div></div></div><div id=":Ruta6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 cDCIeg"></div><div class="Box-sc-g0xbh4-0 dIEiEC">func</div></div>  <div title="__delPadding" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">__delPadding</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="7encrypt" role="treeitem" aria-labelledby=":R12ta6naladaj5:" aria-describedby=":R12ta6naladaj5H1: :R12ta6naladaj5H2:" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:2"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"><div class="PRIVATE_TreeView-item-level-line"></div></div></div><div id=":R12ta6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 cDCIeg"></div><div class="Box-sc-g0xbh4-0 dIEiEC">func</div></div>  <div title="encrypt" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">encrypt</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="8decrypt" role="treeitem" aria-labelledby=":R16ta6naladaj5:" aria-describedby=":R16ta6naladaj5H1: :R16ta6naladaj5H2:" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:2"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"><div class="PRIVATE_TreeView-item-level-line"></div></div></div><div id=":R16ta6naladaj5:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 brdoto"><div class="Box-sc-g0xbh4-0 cDCIeg"></div><div class="Box-sc-g0xbh4-0 dIEiEC">func</div></div>  <div title="decrypt" class="Truncate__StyledTruncate-sc-23o1d2-0 iQHhGT"><span class="Text-sc-17v1xeu-0 gPDEWA">decrypt</span></div></div></span></div></div></li></ul></li></ul></div></div></div></div></div></div> <!-- --> <!-- --> </div></div></div><div class="Box-sc-g0xbh4-0"></div></div></div></div></div><div id="find-result-marks-container" class="Box-sc-g0xbh4-0 aZrVR"></div><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+F6,Control+Shift+F6"></button><button hidden="" data-hotkey="Control+F6,Control+Shift+F6"></button></div> <!-- --> <!-- --> <!-- --> <script type="application/json" id="__PRIMER_DATA__">{"resolvedServerColorMode":"night"}</script></div>
</react-app>




  </div>

</turbo-frame>

    </main>
  </div>

  </div>

          <footer class="footer pt-8 pb-6 f6 color-fg-muted p-responsive" role="contentinfo" hidden="">
  <h2 class="sr-only">Footer</h2>

  


  <div class="d-flex flex-justify-center flex-items-center flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap">
    <div class="d-flex flex-items-center flex-shrink-0 mx-2">
      <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-2" href="https://github.com/">
        <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
</a>
      <span>
        © 2024 GitHub,&nbsp;Inc.
      </span>
    </div>

    <nav aria-label="Footer">
      <h3 class="sr-only" id="sr-footer-heading">Footer navigation</h3>

      <ul class="list-style-none d-flex flex-justify-center flex-wrap mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link--secondary Link">Terms</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link--secondary Link">Privacy</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security" data-view-component="true" class="Link--secondary Link">Security</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}" href="https://www.githubstatus.com/" data-view-component="true" class="Link--secondary Link">Status</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to docs&quot;,&quot;label&quot;:&quot;text:docs&quot;}" href="https://docs.github.com/" data-view-component="true" class="Link--secondary Link">Docs</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}" href="https://support.github.com/?tags=dotcom-footer" data-view-component="true" class="Link--secondary Link">Contact</a>
          </li>

          <li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement">
      Manage cookies
    </button>
  </cookie-consent-link>
</li>

<li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement">
      Do not share my personal information
    </button>
  </cookie-consent-link>
</li>

      </ul>
    </nav>
  </div>
</footer>




    <cookie-consent id="cookie-consent-banner" class="position-fixed bottom-0 left-0" style="z-index: 999999" data-initial-cookie-consent-allowed="" data-cookie-consent-required="false" data-catalyst=""></cookie-consent>


  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden="">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog"></template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;"></div>
</div>

    <template id="snippet-clipboard-copy-button"></template>
<template id="snippet-clipboard-copy-button-unpositioned"></template>


    <style>
      .user-mention[href$="/Mo23fathi"] {
        color: var(--color-user-mention-fg);
        background-color: var(--color-user-mention-bg);
        border-radius: 2px;
        margin-left: -2px;
        margin-right: -2px;
        padding: 0 2px;
      }
    </style>


    </div>

    <div id="js-global-screen-reader-notice" class="sr-only" aria-live="polite" aria-atomic="true">encrypt-decrypt-pdf-file-with-AES256-/AES256.py at main · helmii18/encrypt-decrypt-pdf-file-with-AES256-</div>
    <div id="js-global-screen-reader-notice-assertive" class="sr-only" aria-live="assertive" aria-atomic="true"></div>
  


<script type="text/javascript" src="chrome-extension://nogempgplicnckhcmgjjjgflmipmbgaf/variables-sharing.js"></script><div class="sr-only" id="screenReaderAnnouncementDiv" role="alert" aria-live="assertive"></div></body></html>