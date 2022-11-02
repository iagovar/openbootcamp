        function unaFuncion() {
            console.log(this);

            // Se puede pasar a string con .toString()
            return this;
        }

        const unString = "Esto es un string"

        // Probando bind()

        /*
        https://www.w3schools.com/js/js_function_bind.asp

        En el curso de OB se usa para cambiar el pointer "this" del objeto window a un objeto definido en el parámetro de bind()
        */

        const primerVinculado = unaFuncion.bind(unString);

        primerVinculado()

        console.log(primerVinculado().toString())