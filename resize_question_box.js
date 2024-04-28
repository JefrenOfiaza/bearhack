function resize_question_box(){
    var textarea = document.getElementById("symptoms");
    var question_box = document.getElementById("question_box");
    question_box.style.height = textarea.scrollHeight + "px";
}