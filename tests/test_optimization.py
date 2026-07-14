import unittest
from unittest.mock import patch, MagicMock
from auto_prompt_architect.optimization import OptikOptimizer, LangChainOptimizer, LangGraphOptimizer, HaystackOptimizer
from langchain import LLMChain
from langgraph import GraphDB
from haystack import DocumentStore
from opik import OpikClient
import pydantic
from pydantic import BaseModel
from prometheus_client import Counter

class TestOptimization(unittest.TestCase):

    def test_optik_optimizer(self):
        opik_client = OpikClient()
        optimizer = OptikOptimizer(opik_client)
        prompt = "Test prompt"
        optimized_prompt = optimizer.optimize(prompt)
        self.assertNotEqual(prompt, optimized_prompt)

    def test_langchain_optimizer(self):
        llm_chain = LLMChain()
        optimizer = LangChainOptimizer(llm_chain)
        prompt = "Test prompt"
        optimized_prompt = optimizer.optimize(prompt)
        self.assertNotEqual(prompt, optimized_prompt)

    def test_langgraph_optimizer(self):
        graph_db = GraphDB()
        optimizer = LangGraphOptimizer(graph_db)
        prompt = "Test prompt"
        optimized_prompt = optimizer.optimize(prompt)
        self.assertNotEqual(prompt, optimized_prompt)

    def test_haystack_optimizer(self):
        document_store = DocumentStore()
        optimizer = HaystackOptimizer(document_store)
        prompt = "Test prompt"
        optimized_prompt = optimizer.optimize(prompt)
        self.assertNotEqual(prompt, optimized_prompt)

    @patch('opik.OpikClient')
    def test_optik_optimizer_error(self, mock_opik_client):
        mock_opik_client.side_effect = Exception('Test error')
        optimizer = OptikOptimizer(mock_opik_client)
        prompt = "Test prompt"
        with self.assertRaises(Exception):
            optimizer.optimize(prompt)

    @patch('langchain.LLMChain')
    def test_langchain_optimizer_error(self, mock_llm_chain):
        mock_llm_chain.side_effect = Exception('Test error')
        optimizer = LangChainOptimizer(mock_llm_chain)
        prompt = "Test prompt"
        with self.assertRaises(Exception):
            optimizer.optimize(prompt)

    @patch('langgraph.GraphDB')
    def test_langgraph_optimizer_error(self, mock_graph_db):
        mock_graph_db.side_effect = Exception('Test error')
        optimizer = LangGraphOptimizer(mock_graph_db)
        prompt = "Test prompt"
        with self.assertRaises(Exception):
            optimizer.optimize(prompt)

    @patch('haystack.DocumentStore')
    def test_haystack_optimizer_error(self, mock_document_store):
        mock_document_store.side_effect = Exception('Test error')
        optimizer = HaystackOptimizer(mock_document_store)
        prompt = "Test prompt"
        with self.assertRaises(Exception):
            optimizer.optimize(prompt)

class TestOptimizationMetrics(unittest.TestCase):

    def test_optimization_counter(self):
        counter = Counter('optimization_count', 'Number of optimizations')
        counter.inc()
        self.assertEqual(counter._value.get(), 1)

if __name__ == '__main__':
    unittest.main()