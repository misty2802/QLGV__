/* This JavaScript code snippet is adding event listeners to certain elements on the page when the DOM
content has finished loading. Here's a breakdown of what the code is doing: */
document.addEventListener("DOMContentLoaded", function () {
    const editButtons = document.querySelectorAll(".btn_act.btn_upd");

    editButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            const row = this.closest("tr");
            const cells = row.getElementsByTagName("td");
            const instructorID = this.getAttribute('data-instructor-id');
            if (cells && cells.length >= 12) {
                document.getElementById("instructorID_edit").value = instructorID; 
                /* This line of code is setting the `src` attribute of an image element with the id
                "avt_edit" to the value of the `data-image-url` attribute of the second cell in the
                current row. */
                document.getElementById("avt_preview").src =  cells[2].dataset.imageUrl;
                document.getElementById("name_edit").value = cells[3].textContent;
                document.getElementById("gender_edit").value = cells[4].textContent;
                document.getElementById("birthdate_edit").value = cells[5].getAttribute('data-date-of-birth');
                document.getElementById("phonenumber_edit").value = cells[6].textContent;
                document.getElementById("placeoforigin_edit").value = cells[7].textContent;
                document.getElementById("email_edit").value = cells[8].textContent;
                document.getElementById("department_edit").value =  cells[9].textContent;
                document.getElementById("education_edit").value = cells[10].textContent;
                document.getElementById("position_edit").value = cells[11].textContent;
                document.getElementById("status_edit").value = cells[12].textContent;
              
            } else {
                console.error("Invalid number of cells or cells is undefined.");
            }
            console.log("Row:", row);
            console.log("Cells:", cells); 
        });
    });
    const deleteButtons = document.querySelectorAll(".btn_act.btn_del");

    deleteButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            const instructorID = this.getAttribute('data-instructor-id');
            const deleteConfirmationModal = document.getElementById("deleteConfirmationModal");
            const instructorIdInput = deleteConfirmationModal.querySelector("#instructor_id");
            instructorIdInput.value = instructorID;
            console.log("Instructor ID for deletion:", instructorID); // Log để kiểm tra
        });
    });
   
});