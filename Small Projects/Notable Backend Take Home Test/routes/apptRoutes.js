const router = require('express').Router();
let Appt = require('../models/apptModel');

router.route('/').get((req, res) => {
    Appt.find()
      .then(appt => res.json(appt))
      .catch(err => res.status(400).json('Error: ' + err));
  });


router.route('/add').post((req, res) => {
    const id = req.body.id;
    const patient_first_name = req.body.patient_first_name;
    const patient_last_name = req.body.patient_last_name;
    const datetime = req.body.date;
    const kind = req.body.kind;
    const doctor_id = req.body.doctor_id;

    const newAppt = new Appt({ id, patient_first_name, patient_last_name, datetime, kind, doctor_id });

    newAppt.save()
        .then(() => res.json('Appt added!'))
        .catch(err => res.status(400).json('Error: ' + err));
});


router.route('/:doctorId').get((req, res) => {
    Appt.findById(req.params.doctor_id)
        .then(appt => res.json(appt))
        .catch(err => res.status(400).json('Error: ' + err));
});

router.route('/:date').get((req, res) => {
    Appt.findById(req.params.date)
        .then(appt => res.json(appt))
        .catch(err => res.status(400).json('Error: ' + err));
});

router.route('/:id').delete((req, res) => {
    Appt.findByIdAndDelete(req.params.id)
        .then(() => res.json('Appt deleted'))
        .catch(err => res.status(400).json('Error: ' + err));
});

router.route('/update/:id').post((req, res) => {
    Appt.findById(req.params.id)
        .then(appt => {
            appt.id = req.body.id;
            appt.patient_first_name = req.body.patient_first_name;
            appt.patient_last_name = req.body.patient_last_name;
            appt.datetime = req.body.datetime;
            appt.kind = req.body.kind;
            appt.doctor_id = req.body.doctor_id;

            appt.save()
                .then(() => res.json('Appt updated'))
                .catch(err => res.status(400).json('Error: ' + err));

        })
        .catch(err => res.status(400).json('Error: ' + err));
});
  

module.exports = router;
