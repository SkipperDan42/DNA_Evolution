import dna_dictionaries as dna



skinGenes = {"Skin Type":   dna.skin_types,
             "Skin Tone":   dna.skin_tones,
             "Skin Colour": dna.skin_colours}

bodyGenes = {"Body Type":       dna.body_types,
             "Neck Type":       dna.neck_types,
             "Shoulder Type":   dna.shoulder_types,
             "Chest Shape":     dna.chest_shapes,
             "Waist Type":      dna.waist_types,
             "Hip Type":        dna.hip_types,
             "Heights":         dna.body_types}

hairGenes = {"Hair Texture": dna.hair_textures,
             "Hair Type":    dna.hair_types,
             "Hair Colour":  dna.hair_colours}

bodyHairGenes = {"Hairline Type":   dna.hairline_types,
                 "Eyebrow Type":    dna.eyebrow_types,
                 "Eyelash Type":    dna.eyelash_types,
                 "Body Hair Type":  dna.body_hair_types}

facialGenes = {  "Facial Shape":        dna.facial_shapes,
                 "Forehead Shape":      dna.forehead_shapes,
                 "Eyebrow Shape":       dna.eyebrow_shapes,
                 "Nose Shape":          dna.nose_shapes,
                 "Cheeckbone Shape":    dna.cheekbone_shapes,
                 "Chin Type":           dna.chin_types}

eyeGenes = {"Eye Tone":             dna.eye_tones,
            "Eye Primary Colour":   dna.eye_primary_colours,
            "Eye Secondary Colour": dna.eye_secondary_colours}

eyeShapeGenes = {"Eye Shape":       dna.eye_shapes,
                 "Eyelid Shape":    dna.eyelid_shapes}

lipGenes = {"Smile Type":   dna.smile_types,
            "Lip Shape":    dna.lip_shapes}

teethGenes = {"Teeth Type": dna.teeth_types}

earGenes = {"Ear Size":         dna.ear_sizes,
            "Ear Shape":        dna.ear_shapes,
            "Earlobe Shape":    dna.earlobe_shapes}

armGenes = {"Upper Arm Size":   dna.upper_arm_sizes,
            "Forearm Size":     dna.forearm_sizes,
            "Wrist Size":       dna.wrist_sizes}

handGenes = {"Hand Size":       dna.hand_sizes,
             "Hand Shape":      dna.hand_shapes,
             "Finger Length":   dna.finger_lengths,
             "Nail Shape":      dna.nail_shapes}

legGenes = {"Leg Shape":    dna.leg_shapes,
            "Thigh Size":   dna.thigh_sizes,
            "Calf Size":    dna.calf_sizes}

footGenes = {"Ankle Size":  dna.ankle_sizes,
             "Foot Size":   dna.foot_sizes}

skinPatternGenes = {"Freckle Pattern":      dna.freckle_patterns,
                    "Mole Pattern":         dna.mole_patterns,
                    "Birthmark Pattern":    dna.birthmark_patterns}

voiceGenes = {"Voice": dna.voice_tones}



allGeneClusters = {
            "Skin": skinGenes,
            "Body": bodyGenes,
            "Hair": hairGenes,
            "Body Hair": bodyHairGenes,
            "Face": facialGenes,
            "Eyes":  eyeGenes,
            "Eye Shape": eyeShapeGenes,
            "Lips": lipGenes,
            "Teeth": teethGenes,
            "Ears": earGenes,
            "Arms": armGenes,
            "Hands": handGenes,
            "Legs": legGenes,
            "Feet": footGenes,
            "Skin Patterns": skinPatternGenes,
            "Voice": voiceGenes}