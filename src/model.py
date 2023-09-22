from dataclasses import field

from pydantic import BaseModel, Field

from typing import List, Tuple, Optional, Union


class ISCWSACode(BaseModel):
    code: Optional[str] = Field(alias='Code')
    term_description: Optional[str] = Field(alias='Term Description')
    wt_fn: Optional[Union[float, str]] = Field(alias='Wt.Fn.')
    wt_fn_source: Optional[str] = Field(alias='Wt.Fn. Source')
    type: Optional[str] = Field(alias='Type')
    magnitude: float = Field(alias='Magnitude')
    units: Optional[str] = Field(alias='Units')
    prop: Optional[str] = Field(alias='Prop.')
    p1: int = Field(alias='P1')
    p2: int = Field(alias='P2')
    p3: int = Field(alias='P3')
    wt_fn_comment: Optional[Union[str, float]] = Field(alias='Wt.Fn. Comment')
    depth_formula: Optional[Union[str, int]] = Field(alias='Depth Formula')
    inclination_formula: Optional[Union[str, int]] = Field(alias='Inclination Formula')
    azimuth_formula: Optional[Union[str, int]] = Field(alias='Azimuth Formula')
    singularity_north_formula: Optional[Union[str, float]] = Field(alias='Singularity North Formula')
    singularity_east_formula: Optional[Union[str, float]] = Field(alias='Singularity East Formula')
    singularity_vert_formula: Optional[Union[str, float]] = Field(alias='Singularity Vert. Formula')
    convert_magnitudes_degrees_to_radians: Optional[Union[str, float]] = Field(alias='Convert Magnitudes Degrees to Radians')

    @staticmethod
    def parse_data(tuple_data: Tuple):
        df = tuple_data[1]
        # make a dictionary of the data
        data = df.to_dict()
        return ISCWSACode(**data)



