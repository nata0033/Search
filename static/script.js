var input = document.getElementById("input_field")
var result = document.getElementById("result")

input.oninput = function() {
    input_value = input.value
    query = { input_value }
    query_json = JSON.stringify(query)
    $.ajax({
            url:"/search",
            type:"POST",
            contentType: "application/json",
            data: JSON.stringify(query_json),
            success: function(selected_words) {
                html = ''
                for (let i = 0; i < selected_words["data"].length; i++) {
                    html += '<span>' + selected_words["data"][i] + '</span>'
                    }
                result.innerHTML = html
               }
            });
}
