export interface SkillCategory {
  category: string;
  items: string[];
}

export interface ProjectSchema {
  title: string;
  duration: string;
  description: string[];
  technologies: string[];
}

export interface ExperienceSchema {
  role: string;
  company: string;
  duration: string;
  highlights: string[];
}

export interface ProfileDataResponse {
  name: string;
  title: string;
  contact: {
    email: string;
    phone: string;
    location: string;
    linkedin: string;
  };
  summary: string;
  skills: SkillCategory[];
  experience: ExperienceSchema[];
  projects: ProjectSchema[];
}

export interface AiAgentQueryResponse {
  answer: string;
  context_sources: string[];
}