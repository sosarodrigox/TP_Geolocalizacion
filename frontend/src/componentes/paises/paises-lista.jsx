import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from 'axios'

export default function PaisesLita() {

    const [paises, setPaises] = useState([])

    useEffect(() => {
        getDatos()
    }, [])

    // Formula equivalente con función tradicional sin lambda
    // async function getDatos() {
    //     setPaises(await axios.get('http://localhost:8000/'))
    // }

    const getDatos = async () => {
        let resultado = await axios.get('http://localhost:8000/paises')
        // console.log(resultado)
        setPaises(resultado.data)
    }



    return (
        <>
            <div className="Container-fluid">
                <h1 className="mt-3 tect-center">Paises</h1>
                <table className="table">
                    <thead>
                        <tr>
                            <th>Id</th>
                            <th>Nombre</th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            //Por cada elemento voy a hacer una fila, cada uno tiene que tener un "key" unico
                            //àra eso usamos el id del pais que sabemos que es unico
                            paises.map((pais, idx) => (
                                <tr key={pais.id}>
                                    <td><Link to={"" + pais.id}>
                                        {pais.id}
                                    </Link>
                                    </td>
                                    <td>
                                        {pais.nombre}
                                    </td>
                                </tr>
                            ))
                        }
                    </tbody>
                </table>
                <button className="btn btn-primary">Agregar país</button>

            </div>
        </>)
}