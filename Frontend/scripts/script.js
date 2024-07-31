const submit_button_form = document.getElementById("submit_form_button");
const headline_export_button = document.getElementById("export-button");

headline_export_button.addEventListener("click", function () {
    console.log("working");
    submit_button_form.click();

});



// Dark Mode
const toggle_dark_mode_button = document.getElementById("dark_mode_toggle")
const header_colorChange=document.getElementsByClassName("main_header_tab_flexP");


toggle_dark_mode_button.addEventListener('click', ()=> {
    
    document.body.classList.toggle("dark-mode");
    header_colorChange[0].classList.toggle("main_header_tab_backgroundChange");
   
});

// file adding logic

const file_add=document.getElementById('myFile')
// Note
// Can't use arrow function as arrow function doesn't inherit the this .
file_add.addEventListener('change', function(){
    var fileName = this.files.length ? this.files[0].name : 'No File Chosen';
    document.getElementById('file-name').textContent = fileName;
});


// Handling the drop Features on Web Page
const dropArea = document.getElementById('drop-area');
const drop_action=['dragenter', 'dragover', 'dragleave', 'drop'];


// Prevent default behavior (Prevent file from being opened)
function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

const handledrop=(e)=>{
    let datafile=e.dataTransfer.files;
    handlefile(datafile);
}

const handlefile=(datafile)=>{
  if(datafile.length> 0){
    document.getElementById('file-name').textContent = datafile[0].name;
  }else{
    document.getElementById('file-name').textContent = 'No file chosen';
  }
}

drop_action.forEach((eventname=>{
    dropArea.addEventListener(eventname,preventDefaults,false);
}))

const drag_action=[drop_action[0],drop_action[1]];
const drop_action_child=[drop_action[2],drop_action[3]];

drag_action.forEach(eventName => {
    dropArea.addEventListener(eventName, () => {
        dropArea.classList.add('hover');
    }, false);
});

drop_action_child.forEach(eventName => {
    dropArea.addEventListener(eventName, () => {
        dropArea.classList.remove('hover');
    }, false);
});

dropArea.addEventListener('drop',handledrop,false);



