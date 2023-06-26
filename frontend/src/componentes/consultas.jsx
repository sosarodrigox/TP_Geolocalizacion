import React from "react";
import { NavLink } from "react-router-dom";

export default function Consultas() {
    return (
        <>
            <ul className="nav">
                <li className="nav-item"><NavLink to='provXpais' className='nav-link'>Províncias por país</NavLink></li>
            </ul>
        </>
    )
}