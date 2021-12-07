import React from 'react';

import { Section, SectionText, SectionTitle } from '../../styles/GlobalComponents';
import Button from '../../styles/GlobalComponents/Button';
import { LeftSection } from './HeroStyles';

const Hero = () => (
    <Section row nopadding>
        <LeftSection>
            <SectionTitle main center>
                Full Stack Development
            </SectionTitle>
            <hr />
            <br/>
            <br/>
            <SectionText>
                My friends and family call me a crazy workaholic, but I don't consider it in a bad way. 
                <br/>
                <br/>
                I love maximizing productivity, efficiency, and the feeling of accomplishment. 
            </SectionText>
            <Button onClick={() => window.location = "/docs/resume.pdf"}>Resume</Button>
        </LeftSection>
    </Section>
);

export default Hero;
