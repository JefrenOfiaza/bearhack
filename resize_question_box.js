function resize_question_box(){
    var textarea = document.getElementById("symptoms");
    var question_box = document.getElementById("question_box");
    var new_question_box_height = textarea.scrollHeight;

    textarea.style.height = "auto";
    textarea.style.height = (textarea.scrollHeight-20) + "px";
    question_box.style.height = textarea.scrollHeight + "px";
    max_line_count += 1;
}