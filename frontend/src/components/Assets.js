import React from "react";

const Assets = ({ assets }) => {
    return (
        <div className="section assets">
            <h3>Assets</h3>
            <ul>
                <li>Land: ${assets.land}</li>
                <li>Equipment: ${assets.equipment}</li>
            </ul>
        </div>
    );
};

export default Assets;
