from dataclasses import field

from pydantic import BaseModel, Field

from typing import List


class ISCWSAModel(BaseModel):
    code: List[str] = Field(alias='Code')
    term_description: List[str] = Field(alias='Term Description')
    wt_fn: List[str] = Field(alias='WT Fn')
    wt_fn_source: List[str] = Field(alias='WT Fn Source')
    type: List[str] = Field(alias='Type')
    magnitude: List[str] = Field(alias='Magnitude')
    units: List[str] = Field(alias='Units')
    prop: List[str] = Field(alias='Prop')
    p1: List[str] = Field(alias='P1')
    p2: List[str] = Field(alias='P2')
    p3: List[str] = Field(alias='P3')
    wt_fn_comment: List[str] = Field(alias='WT Fn Comment')
    depth_formula: List[str] = Field(alias='Depth Formula')
    inclination_formula: List[str] = Field(alias='Inclination Formula')
    azimuth_formula: List[str] = Field(alias='Azimuth Formula')
    singularity_north_formula: List[str] = Field(alias='Singularity North Formula')
    singularity_east_formula: List[str] = Field(alias='Singularity East Formula')
    singularity_vert_formula: List[str] = Field(alias='Singularity Vert Formula')
    convert_magnitudes_degrees_to_radians: List[str] = Field(alias='Convert Magnitudes Degrees to Radians')
