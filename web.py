HTMLCode = """
            <head>
                <link href="https://fonts.cdnfonts.com/css/vegapunk" rel="stylesheet">
                <link href="https://fonts.cdnfonts.com/css/dustismo" rel="stylesheet">

                
            </head>
            <style>
            @import url('https://fonts.cdnfonts.com/css/vegapunk');
            @import url('https://fonts.cdnfonts.com/css/dustismo');
            h1{
                font-family:"Vegapunk", sans-serif;
            }
            p{
               font-family: 'Dustismo', sans-serif;
                                                                                
            }
            </style>
            <div style="text-align: center; margin: 0 auto;">
              <div
                style="
                  display: inline-flex;
                  align-items: center;
                  gap: 0.8rem;
                  font-size: 1.75rem;
                "
              >
              <img src="https://seeklogo.com/images/U/ural-federal-university-logo-C368E954BC-seeklogo.com.png" style="height: 50px;" />
                <h1 style="font-size: 50px; font-weight: 1200; margin-bottom: 7px;margin-top:5px;">
                  AlternoVation
                </h1>
              <img src="https://td-alterna.ru/design/alterna/images/logo_alt.svg" style="width: 50px; height: 50px; object-fit: cover; object-position: 0% 0" />
              </div>
              <p style="margin-bottom: 10px; font-size: 20px; line-height: 23px;">
                "Take your office game up a notch - upgrade your workspace with ease & boost productivity on a budget!"
              </p>
            </div>
            
        """

footCode = """
<p align="center">
<iframe title="Report Section" width="720" height="480" 
                src="https://app.powerbi.com/view?r=eyJrIjoiMTdjZWQ3ZmYtYzJkMy00YWM0LWFlODktNzkwOGU2NGU5ZDIyIiwidCI6ImYyM2M2Y2Y4LTVjY2MtNDhmMy04NzgzLWY3NWM3YzlkNjVkZiIsImMiOjl9" 
                frameborder="0"
                align="center" 
                allowFullScreen="true">
            </iframe>
            </p>
"""

CSSCode = """
        .gradio-container {
            font-family: 'IBM Plex Sans', sans-serif;
        }
        .gr-button {
            color: white;
            border-color: black;
            background: black;
        }
        input[type='range'] {
            accent-color: black;
        }
        .dark input[type='range'] {
            accent-color: #dfdfdf;
        }
        .container {
            max-width: 730px;
            margin: auto;
            padding-top: 1.5rem;
        }
        #gallery {
            min-height: 22rem;
            margin-bottom: 15px;
            margin-left: auto;
            margin-right: auto;
            border-bottom-right-radius: .5rem !important;
            border-bottom-left-radius: .5rem !important;
        }
        #gallery>div>.h-full {
            min-height: 20rem;
        }
        .details:hover {
            text-decoration: underline;
        }
        .gr-button {
            white-space: nowrap;
        }
        .gr-button:focus {
            border-color: rgb(147 197 253 / var(--tw-border-opacity));
            outline: none;
            box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
            --tw-border-opacity: 1;
            --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
            --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(3px var(--tw-ring-offset-width)) var(--tw-ring-color);
            --tw-ring-color: rgb(191 219 254 / var(--tw-ring-opacity));
            --tw-ring-opacity: .5;
        }
        #advanced-btn {
            font-size: .7rem !important;
            line-height: 19px;
            margin-top: 12px;
            margin-bottom: 12px;
            padding: 2px 8px;
            border-radius: 14px !important;
        }
        #advanced-options {
            display: none;
            margin-bottom: 20px;
        }
        .footer {
            margin-bottom: 45px;
            margin-top: 35px;
            text-align: center;
            border-bottom: 1px solid #e5e5e5;
        }
        .footer>p {
            font-size: .8rem;
            display: inline-block;
            padding: 0 10px;
            transform: translateY(10px);
            background: white;
        }
        .dark .footer {
            border-color: #303030;
        }
        .dark .footer>p {
            background: #0b0f19;
        }
        .acknowledgments h4{
            margin: 1.25em 0 .25em 0;
            font-weight: bold;
            font-size: 115%;
        }
        .animate-spin {
            animation: spin 1s linear infinite;
        }
        @keyframes spin {
            from {
                transform: rotate(0deg);
            }
            to {
                transform: rotate(360deg);
            }
        }
        #share-btn-container {
            display: flex; padding-left: 0.5rem !important; padding-right: 0.5rem !important; background-color: #000000; justify-content: center; align-items: center; border-radius: 9999px !important; width: 13rem;
            margin-top: 10px;
            margin-left: auto;
        }
        #share-btn {
            all: initial; color: #ffffff;font-weight: 600; cursor:pointer; font-family: 'IBM Plex Sans', sans-serif; margin-left: 0.5rem !important; padding-top: 0.25rem !important; padding-bottom: 0.25rem !important;right:0;
        }
        #share-btn * {
            all: unset;
        }
        #share-btn-container div:nth-child(-n+2){
            width: auto !important;
            min-height: 0px !important;
        }
        #share-btn-container .wrap {
            display: none !important;
        }
        
        .gr-form{
            flex: 1 1 50%; border-top-right-radius: 0; border-bottom-right-radius: 0;
        }
        #prompt-container{
            gap: 0;
        }
        #prompt-text-input, #negative-prompt-text-input{padding: .45rem 0.625rem}
        #component-16{border-top-width: 1px!important;margin-top: 1em}
        .image_duplication{position: absolute; width: 100px; left: 50px}

        footer {visibility: hidden}
"""