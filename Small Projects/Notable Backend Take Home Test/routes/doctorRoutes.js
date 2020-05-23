const router = require('express').Router();
let Doctor = require('../models/doctorModel');

router.route('/').get((req, res) => {
    Doctor.find()
      .then(doctors => res.json(doctors))
      .catch(err => res.status(400).json('Error: ' + err));
  });
  
router.route('/add').post((req, res) => {
    const id = req.body.id;
    const first_name = req.body.first_name;
    const last_name = req.body.last_name;
    
    const newDoctor = new Doctor({ id, first_name, last_name });

    newDoctor.save()
        .then(() => res.json('Doctor added!'))
        .catch(err => res.status(400).json('Error: ' + err));
});


router.route('/:id').get((req, res) => {
    Doctor.findById(req.params.id)
        .then(doctor => res.json(doctor))
        .catch(err => res.status(400).json('Error: ' + err));
});

router.route('/:id').delete((req, res) => {
    Doctor.findByIdAndDelete(req.params.id)
        .then(() => res.json('Doctor deleted'))
        .catch(err => res.status(400).json('Error: ' + err));
});

router.route('/update/:id').post((req, res) => {
    Doctor.findById(req.params.id)
        .then(doctor => {
            doctor.id = req.body.id;
            doctor.first_name = req.body.first_name;
            doctor.last_name = req.body.last_name;

            doctor.save()
                .then(() => res.json('Doctor updated'))
                .catch(err => res.status(400).json('Error: ' + err));

        })
        .catch(err => res.status(400).json('Error: ' + err));
});

module.exports = router;