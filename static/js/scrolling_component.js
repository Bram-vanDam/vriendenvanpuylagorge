    // Function to generate hyperlinks based on the output dictionary
    (function(global, $) {
        function generateLinks(container, dictionary) {
          console.log('DEBUG: generateLinks called with dictionary:', dictionary);
          container.innerHTML = '';
          for (let name in dictionary) {
            if (dictionary.hasOwnProperty(name)) {
              const link = document.createElement('a');
              link.href = dictionary[name];
              link.textContent = name;
              link.target = "_blank";
              container.appendChild(link);
              console.log('DEBUG: Created link:', name, '->', dictionary[name]);
            }
          }
          console.log('DEBUG: Total links generated:', container.children.length);
        }
      
        function initScrollingComponent(opts) {
          console.log('DEBUG: initScrollingComponent called with options:', opts);
          
          // opts.containerId, opts.initialDict (JS object), opts.ajaxUrl
          const container = document.getElementById(opts.containerId);
          console.log('DEBUG: Found container:', container);
          
          // 1) render initial links (if you want)
          
          
          // 2) fetch updated ones via AJAX with cache-busting
          const params = { ...opts.initialDict, _t: Date.now() };
          console.log('DEBUG: Making AJAX request to:', opts.ajaxUrl);
          console.log('DEBUG: Request parameters:', params);
          console.log('DEBUG: Request URL will be:', opts.ajaxUrl + '?' + new URLSearchParams(params).toString());
          
          const startTime = Date.now();
          $.get(opts.ajaxUrl, params)
           .done((data) => {
             const endTime = Date.now();
             console.log('DEBUG: AJAX request completed successfully in', endTime - startTime, 'ms');
             console.log('DEBUG: Raw response data:', data);
             console.log('DEBUG: Response data type:', typeof data);
             
             const out = typeof data === 'string' ? JSON.parse(data) : data;
             console.log('DEBUG: Parsed response data:', out);
             console.log('DEBUG: Number of items in response:', Object.keys(out).length);
             
             generateLinks(container, out);
           })
           .fail((err) => {
             console.error('DEBUG: AJAX request failed:', err);
             console.error('DEBUG: Error status:', err.status);
             console.error('DEBUG: Error statusText:', err.statusText);
             console.error('DEBUG: Error responseText:', err.responseText);
           })
           .always(() => {
             console.log('DEBUG: AJAX request lifecycle completed');
           });
        }
      
        // expose globally
        global.initScrollingComponent = initScrollingComponent;
      
      })(window, jQuery);



// function generateLinks(dictionary) {
//     const container = document.getElementById('scrollContainer');
//     container.innerHTML = ''; // Clear previous links if any

//     // Loop through the dictionary and create an <a> element for each entry
//     for (let name in dictionary) {
//         if (dictionary.hasOwnProperty(name)) {
//             const link = document.createElement('a');
//             link.href = dictionary[name];
//             link.textContent = name;
//             link.target = "_blank"; // Open in a new tab
//             container.appendChild(link);
//         }
//     }
// }

// // Call generateLinks() directly using the dictionary passed from Django
// $(function() {
//     const raw = document.getElementById('input-data')?.textContent;
//     console.log("raw JSON from template:", raw);
//     console.log("TEST")
// const inputDictionary = JSON.parse(
//     document.getElementById('input-data').textContent
// ); // Get input dictionary from Django template

// console.log(inputDictionary); // Log the input dictionary for debugging

// // Make an AJAX request to fetch the output dictionary based on the input
// $.ajax({
//     url: "surveylinks",
//     method: "GET",
//     data: inputDictionary ,  // Send the input dictionary
//     success: function(data) {
//         // Assuming the server returns the output dictionary
//         console.log("output")
//         console.log(data); // Log the output dictionary for debugging
//         generateLinks(JSON.parse(data)); // Generate the links from the output dictionary
//     },
//     error: function(error) {
//         console.error("Error fetching links:", error);
//     }
// });
// })

