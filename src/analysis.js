// detect a change in a file input with an id of “the-file-input”
$("#the-file-input").change(function() {
    // will log a FileList object, view gifs below
    console.log(this.files);
});